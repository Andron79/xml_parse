import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from app.forms import T_ProceduresForm
from app.models import T_Procedures, T_Users
from app.parser import parse_xml_data_to_list


class ParserView(TemplateView):
    model = T_Procedures

    def get(self, request, *args, **kwargs):
        for xml_data_dict in parse_xml_data_to_list():
            T_Procedures.objects.create(
                xml_type=xml_data_dict['xml_type'],
                purchaseNumber=int(xml_data_dict['purchaseNumber']),
                docPublishDate=datetime.datetime.strptime(xml_data_dict['docPublishDate'], '%Y-%m-%dT%H:%M:%S.%f%z'),
                purchaseObjectInfo=xml_data_dict['purchaseObjectInfo'],
                regNum=int(xml_data_dict['regNum']),
                maxPrice=int(xml_data_dict['maxPrice'])
            )

        return HttpResponse('All xml files parsed!!')


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
            print(result_list)
        return self.render_to_response(
            {
                'result_list': result_list,
                'form': form
            }
        )
