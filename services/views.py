from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.views.generic.edit import CreateView

from .forms import PartSaleForm, ServiceRecordForm, WheelServiceForm
from .models import PartSale, ServiceRecord, WheelService


def service_detail(request, pk):
    service = get_object_or_404(ServiceRecord, pk=pk)
    return render(
        request,
        'services/service_detail.html',
        {'service': service},
    )


def service_list(request):
    services = ServiceRecord.objects.all().order_by('-date')

    query = request.GET.get('q')
    if query:
        services = services.filter(car_plate__icontains=query)

    tech = request.GET.get('technician')
    if tech:
        services = services.filter(technician=tech)

    wheels = WheelService.objects.all().order_by('-date')
    parts = PartSale.objects.all().order_by('-date')

    context = {
        'services': services,
        'wheels': wheels,
        'parts': parts,
    }
    return render(request, 'services/service_list.html', context)


def service_create(request):
    if request.method == 'POST':
        form = ServiceRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services:service_list')
    else:
        form = ServiceRecordForm()

    return render(request, 'services/add_service.html', {'form': form})


class ServiceRecordCreateView(CreateView):
    model = ServiceRecord
    form_class = ServiceRecordForm
    template_name = 'services/form_template.html'
    success_url = reverse_lazy('services:service_list')


class WheelServiceCreateView(CreateView):
    model = WheelService
    form_class = WheelServiceForm
    template_name = 'services/form_template.html'
    success_url = reverse_lazy('services:service_list')


class PartSaleCreateView(CreateView):
    model = PartSale
    form_class = PartSaleForm
    template_name = 'services/form_template.html'
    success_url = reverse_lazy('services:service_list')


class ServiceUpdateView(UpdateView):
    model = ServiceRecord
    fields = '__all__'
    template_name = 'services/form_template.html'
    success_url = reverse_lazy('services:service_list')


class ServiceDeleteView(DeleteView):
    model = ServiceRecord
    template_name = 'services/confirm_delete.html'
    success_url = reverse_lazy('services:service_list')
