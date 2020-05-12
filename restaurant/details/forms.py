from django import forms


class Register(forms.Form):
    choices = [('customer', 'Customer'), ('manager', 'Manager'),
               ]
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    details = forms.CharField(widget=forms.Textarea(attrs={'style':"width:100%"}), required=False)
    type = forms.ChoiceField(widget=forms.Select(attrs={"class":"form-control"}), choices=choices)


class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))