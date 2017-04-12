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
loadPage: function(url){
	var fetch = true;
	var data = {};
	{% if storage %}
	if (this.isInStorage(resturl) === true) {
		//console.log("Data in storage: "+resturl);
		data = this.loadFromStorage(url);
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
		var q = 'query{page(url:"'+url+'"){url,title,content,extraData}}';
		function error() {
			app.pageContent = "<h1>An error has occured</h1>";
			top.document.title = "Error";
		}
		function action(data) {
			app.pageContent = data.page.content;
			top.document.title = data.page.title;
		}
		app.flush();
		app.activate(["pageContent"]);
		
		runQuery(q, action, error);

	    var now = new Date();
		var exp = new Date();
		var mins = 1;
		var duration = 1000*60*mins;
		exp.setTime(now.getTime() + (duration));
		data.expires = exp;
		{% if storage %}
			//console.log("Setting key in local storage");
			store.set(url, data);
		{% endif %}
		{% if perms.vvpages.change_page %}
	    	app.adminPageUrl ="/admin/vvpages/page/"+data.pk+"/change/";
	    {% endif %}
	} else {
		app.flush();
		app.pageContent = data.content;
	    top.document.title = data.title;
	    app.activate(["pageContent"]);
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
	    top.document.title = title;
	    app.activate(["pageContent"]);
	});
	return
},