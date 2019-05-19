from django import forms
from .models import Project, Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length= 50, widget=forms.TextInput())
    email = forms.EmailField(max_length= 255, widget=forms.TextInput())
    subject = forms.CharField(max_length= 50, widget=forms.TextInput())
    message = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Project Name'}))
    category = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Category'}))
    project_info = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Project Info'}))
    clients = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Clients'}))
    tools = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tools'}))
    live_url = forms.URLField(max_length=50, widget=forms.URLInput(attrs={'class':'form-control', 'placeholder':'Live URL'}))

    class Meta:
        model = Project
        fields = [
            'project_name',
            'category',
            'thumb_1',
            'thumb_2',
            'project_info',
            'clients',
            'tools',
            'live_url'
        ]
