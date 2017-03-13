{% load vv_tags %}

isInStorage: function(resturl) {
	var url = store.get(resturl);
	if (url == undefined) {
		return false
	}
	return true
},
loadFromStorage: function(resturl) {
	var url = store.get(resturl);
	console.log("store: "+url);
},
loadHtml: function(resturl){
	if (this.isInStorage(resturl) === true) {
		loadFromStorage(resturl);
	}
	promise.get(resturl,{},{"Accept":"application/json"}).then(function(error, data, xhr) {
	    if (error) {console.log('Error ' + xhr.status);return;}
	    {% if isdebug is True %}console.log("Raw data: "+data);{% endif %}
	    app.flushContent();
	    var data = JSON.parse(data);
	    app.content = data.content;
	    app.title = data.title;
	    top.document.title = data.title;
	});
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