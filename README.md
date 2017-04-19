# Django VVpages

Vue.js pages management for [Django Vite Vue](https://github.com/synw/django-vitevue). 

Features:

- Fast: single page app with Vue.js on the frontend
- Flexible: users can choose which editor to use: Codemirror or Ckeditor, admins can choose who can edit what pages
- Mobile friendly: client side cache and offline mode (optional)

## Install

  ```bash
pip install djangorestframework pytz django-jsonfield django-filter \
django-mptt django-ckeditor django-codemirror2 django-reversion

pip install git+https://github.com/synw/django-vitevue.git
  ```
 
INSTALLED_APPS:

  ```python
"reversion",
"restframework",
"mptt",
"guardian",
"ckeditor",
"ckeditor_uploader",
"codemirror2",
"vv",
"vvpages",
  ```
  
Set the authentication backend: 

  ```python
AUTHENTICATION_BACKENDS = (
    # ...
    'guardian.backends.ObjectPermissionBackend',
)
  ```

Set the urls:

  ```python
urlpatterns = [
	# ...	
	url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^pages/',include('vvpages.urls')),
]

urlpatterns.append(url(r'^',include('vv.urls')))
  ```

Note: an automatic sitemap is available at `/map/`

Import the necessary js libs in head:

  ```html
<script type="text/javascript" src="{% static 'js/vue.min.js' %}"></script>
<script type="text/javascript" src="{% static 'js/page.js' %}"></script>
<script type="text/javascript" src="{% static 'js/axios.min.js' %}"></script>
<!-- if you want to use local storage : -->
<script type="text/javascript" src="{% static 'js/store.legacy.min.js' %}"></script>
  ```
Migrate

### Settings

Settings for ckeditor:

  ```python
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_JQUERY_URL = 'https://cdn.jsdelivr.net/jquery/3.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar':  [
                    ["Format", "Styles", "Bold", "Italic", "Underline", '-', 'RemoveFormat'],
                    ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter','JustifyRight', 'JustifyBlock'],
                    ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'],
                    ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],["Source", "Maximize"],
                    ],
        "removePlugins": "stylesheetparser",
        'width': '1150px',
        'height': '450px',
    },
}
  ```

To use Codemirror instead of Ckeditor by default:

  ```python
VVPAGES_CODE_MODE = True
  ```

## Client cache

The is an option to use the client local storage to cache pages. This make the data available on the 
client even if it is offline. To enable it use the setting:

  ```python
VVPAGES_LOCAL_STORAGE = True
VVPAGES_TTL = 180
  ```
  
The ``VVPAGES_TTL` is optional: this is the number of minutes the cache key will be retained in local storage before
trying to refetch fresh data from the server. Default is set to 60.

Warning: only use this option if you eventual consistency is ok for you

## Templates
 
Main template:

  ```html
<div v-html="content"></div>
{% block vues %}{% endblock %}
  ```
 
 An edit button is available to link to the admin edit interface from pages:
 
   ```django
{% if perms.vvpages.change_page %}
	<a v-bind:href="adminPageUrl" v-show="adminPageUrl">Edit page</a>
{% endif %}
  ```

## Tools

A page creation wizard is available at `/pages/wizard/`

## Installer and demo

You can use the [Django Mogo](https://github.com/synw/django-mogo) installer script to get a demo or an install

## Todo
 
 - [x] Object level permissions
 - [ ] Preview before commit
