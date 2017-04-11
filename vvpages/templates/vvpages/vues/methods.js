{% load vv_tags vvpages_tags %}
{% use_local_storage as storage %}
{% if storage %}
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
{% endif %}
loadHtml: function(resturl){
	var fetch = true;
	var data = {};
	{% if storage %}
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
	{% endif %}
	if (fetch === true){
		//console.log("Fetchind data from "+resturl+" //");
		promise.get(resturl,{},{"Accept":"application/json"}).then(function(error, data, xhr) {
		    if (error) {
		    	console.log('Error ' + xhr.status);return;
		    }
		    {% if isdebug is True %}console.log("Raw data: "+data);{% endif %}
		    data = JSON.parse(data);
			app.flush();
			app.pageContent = data.content;
		    app.pageTitle = data.title;
		    top.document.pageTitle = data.title;
		    app.activate(["pageContent", "pageTitle"]);
		    var now = new Date();
			var exp = new Date();
			var mins = 1;
			var duration = 1000*60*mins;
			exp.setTime(now.getTime() + (duration));
			data.expires = exp;
			{% if storage %}
				//console.log("Setting key in local storage");
				store.set(resturl, data);
			{% endif %}
			{% if perms.vvpages.change_page %}
		    	app.adminPageUrl ="/admin/vvpages/page/"+data.pk+"/change/";
		    {% endif %}
		});
	} else {
		app.flush();
		app.pageContent = data.content;
	    app.pageTitle = data.title;
	    top.document.pageTitle = data.title;
	    app.activate(["pageContent", "pageTitle"]);
	    {% if perms.vvpages.change_page %}
	    	app.adminPageUrl ="/admin/vvpages/page/"+data.pk+"/change/";
	    {% endif %}
	}
	return
},
loadChunk: function (resturl, title){
	promise.get(resturl).then(function(error, data, xhr) {
	    if (error) {console.log('Error ' + xhr.status);return;}
	    {% if isdebug is True %}console.log("Raw chunk: "+data);{% endif %}
	    app.flush();
	    app.pageContent = data;
	    app.pageTitle = title;
	    top.document.title = title;
	    app.activate(["pageContent", "pageTitle"]);
	});
	return
},