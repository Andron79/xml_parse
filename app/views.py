from django.shortcuts import render
from django.views.generic import FormView

from app.forms import T_ProceduresForm
from app.models import T_Procedures


class T_ProceduresView(FormView):
    form_class = T_ProceduresForm
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        result_list = T_Procedures.objects.filter(curator__isnull=False)
        return render(
            request,
            'dashboard.html',
            {
                'result_list': result_list,
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            result_list = T_Procedures.objects.filter(curator__name__contains=form.cleaned_data['curator'])
        else:
            result_list = T_Procedures.objects.filter(curator__isnull=False)
        return self.render_to_response(
            {
                'result_list': result_list,
                'form': form
            }
        )
