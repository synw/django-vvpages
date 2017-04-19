{% load vvpages_tags %}
siteSlug: "{% site_slug %}",
pageContent: "",
{% if perms.vvpages.change_page %}adminPageUrl: "",
showPageForm: false,
pageFormParent: 0,
pageFormTitle: "",
pageFormUrl: "",{% endif %}