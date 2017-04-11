# Django VVpages

Vue.js pages management for [Django Vite Vue](https://github.com/synw/django-vitevue)

## Install

Install Vite Vue. Clone

  ```python
pip install djangorestframework django-ckeditor django-codemirror2
  ```
 
INSTALLED_APPS:

  ```python
"rest_framework",
"mptt",
"ckeditor",
"ckeditor_uploader",
"codemirror2",
"vv",
"vvpages",
  ```

Get the dependencies:

  ```python
pip install pytz django-jsoneditor djangorestframework django-jsonfield django-mptt django-ckeditor django-codemirror2
  ```

Set th urls:

  ```python
urlpatterns = [
	url(r'^pages/',include('vvpages.urls')),
	url(r'^ckeditor/',include('ckeditor_uploader.urls')),
]

urlpatterns.append(url(r'^',include('vv.urls')))
  ```
  
Migrate

Add this to your main template:

  ```html
<div id="content" v-html="content"></div>
  ```

### Settings

Example settings for ckeditor:

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
 
 ## Installer and demo

You can use the [Django Mogo](https://github.com/synw/django-mogo) installer script to get a demo or an install

 ## Todo
 
 - [ ] Object level permissions
 - [ ] Preview before commit
