from django import forms


class CreationForm(forms.Form):
    num = forms.IntegerField(min_value=1, max_value=5,
                             label="Number of variables")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['num'].widget.attrs.update({'class': 'form-control'})


class EquationForm(forms.Form):

    def __init__(self, num, *args, **kwargs):
        super(EquationForm, self).__init__(*args, **kwargs)
        for i in range(num):
            self.fields[f"coef{i}"] = forms.FloatField(label=f'\\(x_{i}\\)')
            self.fields[f"coef{i}"].widget.attrs.update({'class': 'form-control'})
            
