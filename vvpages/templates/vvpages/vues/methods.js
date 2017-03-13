{% load vv_tags %}

isInStorage: function(resturl) {
	var url = store.get(resturl);
	if (url == undefined) {
		return false
	}
	return true
},
loadFromStorage: function(resturl) {
	var data = store.get(resturl);
	return data
},
loadHtml: function(resturl){
	var fetch = true;
	var data = {};
	if (this.isInStorage(resturl) === true) {
		//console.log("Data in storage: "+resturl);
		data = this.loadFromStorage(resturl);
		now = new Date();
		var is_expired = false; 
		if (data.expires < now) {
			var is_expired = true;
		}
		if (is_expired === false) {
			//console.log("Data not expired");
			fetch = false;
		} else {
			//console.log("Data expired");
			if (navigator.onLine === false) {
				fetch = false;
				//console.log("Navigator not online");
			} else {
				//console.log("Navigator online");
			}
		}
	} 
	if (fetch === true){
		//console.log("Fetchind data from "+resturl+" //"+JSON.stringify(data));
		promise.get(resturl,{},{"Accept":"application/json"}).then(function(error, data, xhr) {
		    if (error) {
		    	console.log('Error ' + xhr.status);return;
		    }
		    {% if isdebug is True %}console.log("Raw data: "+data);{% endif %}
		    data = JSON.parse(data);
		});
		var now = new Date();
		var exp = new Date();
		var mins = 24*60;
		var duration = 1000*60*mins;
		exp.setTime(oldDateObj.getTime() + (duration));
		data.expires = exp;
		store.set(resturl, data);
	}
	app.flushContent();
	app.content = data.content;
    app.title = data.title;
    top.document.title = data.title;
	return
},
loadChunk: function (resturl, title){
	promise.get(resturl).then(function(error, data, xhr) {
	    if (error) {console.log('Error ' + xhr.status);return;}
	    {% if isdebug is True %}console.log("Raw chunk: "+data);{% endif %}
	    app.flushContent();
	    app.content = data;
	    app.title = title;
	    top.document.title = title;
	});
	return
},