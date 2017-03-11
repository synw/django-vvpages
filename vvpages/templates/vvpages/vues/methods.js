{% load vv_tags %}

loadHtml: function(resturl){
	promise.get(resturl,{},{"Accept":"application/json"}).then(function(error, data, xhr) {
	    if (error) {console.log('Error ' + xhr.status);return;}
	    {% if isdebug is True %}console.log("Raw data: "+data);{% endif %}
	    console.log("DEBUG {{ debug }}");
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
	    app.content = data;
	    app.title = title;
	    top.document.title = title;
	});
	return
},