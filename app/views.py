import datetime

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from app.forms import T_ProceduresForm
from app.models import T_Procedures
from app.parser import parse_xml_data_to_list


class ParserView(TemplateView):
    model = T_Procedures

    def get(self, request, *args, **kwargs):  # TODO bulk_create()
        for xml_data_dict in parse_xml_data_to_list():
            T_Procedures.objects.create(
                xml_type=xml_data_dict['xml_type'],
                purchaseNumber=int(xml_data_dict['purchaseNumber']),
                docPublishDate=datetime.datetime.strptime(xml_data_dict['docPublishDate'], '%Y-%m-%dT%H:%M:%S.%f%z'),
                purchaseObjectInfo=xml_data_dict['purchaseObjectInfo'],
                regNum=int(xml_data_dict['regNum']),
                maxPrice=int(xml_data_dict['maxPrice'])
            )

        return render(
            request,
            'dashboard.html', )
        # HttpResponse('All xml files parsed!!')


class T_ProceduresView(FormView):
    form_class = T_ProceduresForm
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.GET)
        qs = T_Procedures.objects.filter(curator__isnull=False)
        y_max_sum_list, x_date_list = self.get_axios
        data_set = self.get_dataset(qs)
        return render(
            request,
            'dashboard.html',
            {
                'x_date_list': x_date_list,
                'y_max_sum_list': y_max_sum_list,
                'data_set': data_set,
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            qs = T_Procedures.objects.filter(
                curator__name__contains=form.cleaned_data['curator']).order_by('docPublishDate')
        else:
            qs = T_Procedures.objects.filter(curator__isnull=False).order_by('docPublishDate')
        y_max_sum_list, x_date_list = self.get_axios
        data_set = self.get_dataset(qs)
        return self.render_to_response(
            {
                'x_date_list': x_date_list,
                'y_max_sum_list': y_max_sum_list,
                'data_set': data_set,
                'form': form
            }
        )

    @property
    def get_axios(self):
        qs = T_Procedures.objects.all()
        x_date_list = [str(item.docPublishDate)[:10] for item in qs]
        x_date_list.sort()
        y_max_sum_list = []
        for date in qs:
            y_max_sum_list.append(
                T_Procedures.objects.order_by('docPublishDate').filter(docPublishDate=date.docPublishDate).aggregate(
                    max_sum_date=(Sum('maxPrice')))['max_sum_date'])
        y_max_sum_list = set(y_max_sum_list)
        y_max_sum_list = list(y_max_sum_list)
        y_max_sum_list.sort()
        return y_max_sum_list, x_date_list

    @staticmethod
    def get_dataset(qs):
        data_set = [item.maxPrice for item in qs]
        return data_set
