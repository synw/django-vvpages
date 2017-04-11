# -*- coding: utf-8 -*-

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from vvpages.models import Page
from vvpages.conf import CODE_MODE, CODEMIRROR_KEYMAP
if CODE_MODE == True:
    from codemirror2.widgets import CodeMirrorEditor


class PageAdminWysiForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    content.required = False
    content.label = ""
    
    class Meta:
        model = Page
        exclude = ('edited', 'created', "editor")


class PageAdminCodeForm(forms.ModelForm):
    content = forms.CharField(
          widget=CodeMirrorEditor(options={
                                     'mode':'htmlmixed',
                                     'width':'1170px',
                                     'indentWithTabs':'true', 
                                     #'indentUnit' : '4',
                                     'lineNumbers':'true',
                                     'autofocus':'true',
                                     #'highlightSelectionMatches': '{showToken: /\w/, annotateScrollbar: true}',
                                     'styleActiveLine': 'true',
                                     'autoCloseTags': 'true',
                                     'keyMap': CODEMIRROR_KEYMAP,
                                     'theme':'blackboard',
                                     #'fullScreen':'true',
                                     },
                                     script_template='codemirror2/codemirror_script_vvpages.html',
                                     modes=['css', 'xml', 'javascript', 'htmlmixed'],
                                     )
          
          )
    content.required = False
    content.label = ""
    
    class Meta:
        model = Page
        exclude = ('edited', 'created', "editor")
