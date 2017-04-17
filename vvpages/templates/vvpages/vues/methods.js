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
		axios.get(resturl).then(function (response) {
			var data = response.data;
			{% if isdebug is True %}console.log("Raw data: "+data);{% endif %}
			app.flush();
			app.pageContent = data.content;
		    top.document.title = data.title;
			{% if storage %}
				var now = new Date();
				var exp = new Date();
				var mins = 1;
				var duration = 1000*60*mins;
				exp.setTime(now.getTime() + (duration));
				data.expires = exp;
				//console.log("Setting key in local storage");
				store.set(resturl, data);
			{% endif %}
			{% if perms.vvpages.change_page %}
		    	app.adminPageUrl ="/admin/vvpages/page/"+data.pk+"/change/";
		    	app.activate(["pageContent", "adminPageUrl"]);
		    {% else %}
		    	app.activate(["pageContent"]);
		    {% endif %}
			
		}).catch(function (error) {
			console.log(error);
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
		{% if isdebug is True %}console.log("Raw chunk: "+response.data);{% endif %}
		app.flush();
	    app.pageContent = response.data;
	    top.document.title = title;
	    app.activate(["pageContent"]);
	}).catch(function (error) {
		console.log(error);
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