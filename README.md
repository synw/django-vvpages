# Django VVpages

Vue.js pages management for [Django Vite Vue](https://github.com/synw/django-vitevue)

## Install

Install Vite Vue. Clone
 
INSTALLED_APPS:

  ```python
"rest_framework",
"mptt",
"ckeditor",
"ckeditor_uploader",
"codemirror2",
"jsoneditor",
"vvpages",
  ```

Get the dependencies:

  ```python
pip install pytz django-jsoneditor djangorestframework django-jsonfield django-mptt django-ckeditor django-codemirror2
  ```

Set th urls:

  ```python
url(r'^pages/',include('vvpages.urls')),
url(r'^ckeditor/',include('ckeditor_uploader.urls')),
  ```
  
Migrate

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
