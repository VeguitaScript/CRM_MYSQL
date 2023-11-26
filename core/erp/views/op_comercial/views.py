from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import OpComercialForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import OpComercial


class OpComercialListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = OpComercial
    template_name = 'op_comercial/list.html'
    permission_required = 'erp.view_op_comercial'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in OpComercial.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Oportunidad Comercial'
        context['create_url'] = reverse_lazy('erp:op_comercial_create')
        context['list_url'] = reverse_lazy('erp:op_comercial_list')
        context['entity'] = 'Oportunidad Comercial'
        return context


class OpComercialCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = OpComercial
    form_class = OpComercialForm
    template_name = 'op_comercial/create.html'
    success_url = reverse_lazy('erp:op_comercial_list')
    permission_required = 'erp.add_op_comercial'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Oportunidad Comercial'
        context['entity'] = 'Oportunidad Comercial'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class OpComercialUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = OpComercial
    form_class = OpComercialForm
    template_name = 'op_comercial/create.html'
    success_url = reverse_lazy('erp:op_comercial_list')
    permission_required = 'erp.change_op_comercial'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Oportunidad Comercial'
        context['entity'] = 'Oportunidad Comercial'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class OpComercialDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = OpComercial
    template_name = 'op_comercial/delete.html'
    success_url = reverse_lazy('erp:op_comercial_list')
    permission_required = 'erp.delete_op_comercial'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Oportunidad Comercial'
        context['entity'] = 'Oportunidad Comercial'
        context['list_url'] = self.success_url
        return context