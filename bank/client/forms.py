from django import forms


class UserForm(forms.Form):
    Pib = forms.RegexField(label="ПІБ", regex="[а-я А-Я]")
    Date_of_Birth = forms.DateField(label="Дата рождения")
    Telephone = forms.RegexField(label="Номер телефона", regex="(?:\w)(?:(?:(?:(?:\+?3)?8\W{0,5})?0\W{0,5})?[34569]\s?\d[^\w,;(\+]{0,5})?\d\W{0,5}\d\W{0,5}\d\W{0,5}\d\W{0,5}\d\W{0,5}\d\W{0,5}\d(?!(\W?\d))")
    Email = forms.EmailField(label="Электронная почта")
    adress=  forms.RegexField(label="Адреса", regex="[а-я А-Я 0-9, .]")
    
