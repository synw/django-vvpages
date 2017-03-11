{% load i18n %}
page('/map/', function(ctx, next) { app.loadChunk('{% url "vvpages-map-rest" %}', '{% trans "Sitemap" %}') } );
{% include "vvpages/auto/routes.js" %}