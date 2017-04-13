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
		var fields = "{% if perms.vvpages.change_page %}pageId,{% endif %}url,title,content,extraData";
		var q = 'query{page(url:"'+url+'"){'+fields+'}}';
		function error() {
			app.pageContent = "<h1>An error has occured</h1>";
			top.document.title = "Error";
			app.flush();
			app.activate(["pageContent"]);
		}
		function action(data) {
			app.pageContent = data.page.content;
			top.document.title = data.page.title;
			app.flush();
			{% if perms.vvpages.change_page %}
		    	app.adminPageUrl ="/admin/vvpages/page/"+data.page.pageId+"/change/";
		    	app.activate(["pageContent", "adminPageUrl"]);
		    {% else %}
		    	app.activate(["pageContent"]);
		    {% endif %}
		    console.log(app.str(data));
		}
		runQuery(q, action, error);
		{% if storage %}
			var now = new Date();
			var exp = new Date();
			var mins = 1;
			var duration = 1000*60*mins;
			exp.setTime(now.getTime() + (duration));
			data.expires = exp;
			//console.log("Setting key in local storage");
			store.set(url, data);
		{% endif %}
	} else {
		this.flush();
		this.pageContent = data.content;
	    top.document.title = data.title;
	    this.activate(["pageContent"]);
	    {% if perms.vvpages.change_page %}
	    	this.adminPageUrl ="/admin/vvpages/page/"+data.pk+"/change/";
	    	this.activate(["pageContent", "adminPageUrl"]);
	    {% else %}
	    	this.activate(["pageContent"]);
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