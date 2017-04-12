{% load i18n %}
page('/', function(ctx, next) { app.loadPage(ctx.path) });
page('/map/', function(ctx, next) { app.loadChunk('{% url "vvpages-map-rest" %}', '{% trans "Sitemap" %}') });
page('/:url', function(ctx, next) { app.loadPage(ctx.path) });