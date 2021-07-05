from django import forms

from app.models import T_Users, T_Procedures


class T_ProceduresForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=T_Procedures.objects.filter(curator__isnull=False),
        empty_label='Все кураторы',
        label='Имя',

    )

    # class Meta:
    #     model = T_Users
    #     # fields = ['name', ]
