from django import forms
from .models import *
from django.forms import inlineformset_factory

class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']

class PersonForm(forms.ModelForm):
    labels = forms.ModelMultipleChoiceField(
        queryset=Label.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,  # You can change this to a dropdown with `forms.SelectMultiple`
        label="Existing Labels",
    )
    custom_label = forms.CharField(
        required=False,
        label="Custom Label",
        widget=forms.TextInput(attrs={"placeholder": "Enter a new label (optional)"})
    )

    class Meta:
        model = Person
        fields = ['name', 'image', 'labels', 'custom_label']


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['url', 'description']

# Formset
LinkFormSet = inlineformset_factory(
    Person, Link, form=LinkForm, extra=1, can_delete=True
)