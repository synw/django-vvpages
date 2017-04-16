{% load i18n %}
page('/map/', function(ctx, next) { app.loadChunk('{% url "vvpages-map-rest" %}', '{% trans "Sitemap" %}') });
{% if perms.vvpages.change_page %}page('/pages/wizard/', function(ctx, next) { app.loadChunk('{% url "vvpages-wizard" %}', '{% trans "Pages wizard" %}') });{% endif %}
{% include "vvpages/auto/routes.js" %}