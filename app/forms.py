from django import forms
# from django.db.models import Count

from app.models import T_Procedures


class T_ProceduresForm(forms.Form):
    curator = forms.ModelChoiceField(
        queryset=T_Procedures.objects.filter(curator__isnull=False).order_by().distinct('curator__name'),
        widget=forms.Select(attrs={"onChange": 'submit()'}),
        empty_label='Все кураторы',
        label='Кураторы '
    )
