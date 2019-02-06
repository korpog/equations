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
        for i in range(num + 1):
            if(i == range(num + 1)[-1]):
                self.fields["b"] = forms.FloatField(label=f'\\(b\\)', label_suffix='')
                self.fields["b"].widget.attrs.update(
                    {'class': 'form-control'})
            else:    
                self.fields[f"coef_{i + 1}"] = forms.FloatField(label=f'\\(x_{i + 1}\\)', label_suffix='')
                self.fields[f"coef_{i + 1}"].widget.attrs.update(
                    {'class': 'form-control'})
