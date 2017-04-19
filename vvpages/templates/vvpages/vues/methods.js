{% load vv_tags vvpages_tags %}
{% use_local_storage as storage %}
{% if storage %}
	storeExists: function(resturl) {
		var key = this.siteSlug+"_"+resturl;
		var url = store.get(key);
		if (url == undefined) {
			return false
		}
		return true
	},
	storeGet: function(resturl) {
		var key = this.siteSlug+"_"+resturl;
		var data = store.get(key);
		return data
	},
	storeSet: function(resturl, data) {
		//console.log("RESTURL", resturl);
		var now = new Date();
		var exp = new Date();
		var mins = 1;
		var duration = 1000*60*{% ttl %};
		exp.setTime(now.getTime() + duration);
		data.expires = exp;
		var key = this.siteSlug+"_"+resturl;
		//console.log("S+U", this.siteSlug, resturl);
		//console.log("Setting key", key, "in local storage. \nExpiration:", exp);
		store.set(key, data);
	},
{% endif %}
loadHtml: function(resturl){
	var fetch = true;
	var data = {};
	{% if storage %}
	var key = this.siteSlug+"_"+resturl;
	if (this.storeExists(key) === true) {
		//console.log("Data in storage: "+resturl);
		data = this.storeGet(key);
		if (!data) {
			//console.log("No data", data);
		}
		var now = new Date();
		var is_expired = false;
		var exp = new Date(data.expires);
		var diff = (now - exp);
		//console.log("DATE DIFF:", diff, now, exp);
		if ( diff >= 0 ) {
			is_expired = true;
			store.remove(key);
		}
		if (is_expired === false) {
			//console.log("Data not expired\nExpiration:", data.expires);
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
		axios.get(resturl).then(function (response) {
			var data = response.data;
			{% if isdebug is True %}//console.log("Raw data: "+data);{% endif %}
			app.flush();
			app.pageContent = data.content;
		    top.document.title = data.title;
			{% if storage %}
			//console.log("SLUG", app.siteSlug);
				var key = app.siteSlug+"_"+resturl;	
				//console.log("K", app.siteSlug, key);
				app.storeSet(key, data);
			{% endif %}
			{% if perms.vvpages.change_page %}
		    	app.adminPageUrl ="/admin/vvpages/page/"+data.pk+"/change/";
		    	app.activate(["pageContent", "adminPageUrl"]);
		    {% else %}
		    	app.activate(["pageContent"]);
		    {% endif %}
			
		}).catch(function (error) {
			//console.log(error);
		});
	} else {
		app.flush();
		app.pageContent = data.content;
	    top.document.title = data.title;
	    {% if perms.vvpages.change_page %}
		    app.adminPageUrl ="/admin/vvpages/page/"+data.pk+"/change/";
	    	app.activate(["pageContent", "adminPageUrl"]);
	    {% else %}
	    	app.activate(["pageContent"]);
	    {% endif %}
	}
	return
},
loadChunk: function (resturl, title){
	axios.get(resturl).then(function (response) {
		{% if isdebug is True %}//console.log("Raw chunk: "+response.data);{% endif %}
		app.flush();
	    app.pageContent = response.data;
	    top.document.title = title;
	    app.activate(["pageContent"]);
	}).catch(function (error) {
		//console.log(error);
	});
},
{% if perms.vvpages.change_page %}postPageForm: function() {
	if (isUrl(this.pageFormUrl) !== true) {
		alert("The url must start with /")
		return
	}
	var data = {
		title: this.pageFormTitle,
		url: this.pageFormUrl,
		parent: this.pageFormParent
	};
	function error(err) {
		console.log(err)
	}
	function action(response) {
		app.pageContent = response.data;
		app.pageFormTitle = "";
		app.pageFormUrl = "";
		app.pageFormParent = "";
		app.showPageForm = false;
	}
	this.postForm('{% url "vvpages-wizard-post" %}', data, action, error)
},
popPageForm: function(parent) {
	this.showPageForm = true;
	this.pageFormParent = parent;
	this.flush("pageContent");
	this.activate(["showPageForm", "pageContent"]);
},{% endif %}