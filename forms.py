from django import forms

class Ex1Form(forms.Form):
    lbd = forms.FloatField(label="lbd", required=True, min_value=0.0)
    p01 = forms.FloatField(label="p01", required=True, max_value=1.0, min_value=0.0)
    mu1 = forms.FloatField(label="mu1", required=True, min_value=0.0)
    mu2 = forms.FloatField(label="mu2", required=True, min_value=0.0)
    mu3 = forms.FloatField(label="mu3", required=True, min_value=0.0)

class fileForm(forms.Form):
    nbFiles = forms.IntegerField(label="nbFiles", required=True, min_value=0)
    lbd = forms.FloatField(label="lbd", required=True, min_value=0.0)