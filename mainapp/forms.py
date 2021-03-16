from django import forms


class GetDiscountForm(forms.Form):
    name = forms.CharField(max_length=100, label='')
    phone = forms.CharField(max_length=20, label='')

    name.widget.attrs.update(
        {
            'class': "form-control mb-3",
            'placeholder': 'Как вас зовут',
        }
    )

    phone.widget.attrs.update(
        {
            'class': "form-control mb-3",
            'placeholder': 'Ваш номер телефона',
        }
    )