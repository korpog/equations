from django import forms


class CreationForm(forms.Form):
    num = forms.IntegerField(min_value=1, max_value=5,
                             label="Number of variables")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['num'].widget.attrs.update({'class': 'form-control'})
