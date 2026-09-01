from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from services.models import ServiceRecord, WheelService

User = get_user_model()

# --- Dashboard Views ---


@login_required
def dashboard(request):
    """
    Main dashboard view: redirects mechanics to stats,
    customers to their history.
    """
    # 1. Mechanic Dashboard (Global Stats)
    if request.user.is_staff or getattr(request.user, 'is_mechanic', False):
        total_revenue = (
            ServiceRecord.objects.aggregate(total=Sum('price'))['total'] or 0
        )
        recent_services = ServiceRecord.objects.all().order_by('-date')[:5]
        recent_wheels = WheelService.objects.all().order_by('-date')[:5]

        context = {
            'is_mechanic': True,
            'total_revenue': total_revenue,
            'recent_services': recent_services,
            'recent_wheels': recent_wheels,
            'service_count_today': ServiceRecord.objects.filter(
                date=timezone.now().date()
            ).count(),
            'active_staff_count': User.objects.filter(is_active=True).count(),
        }
        return render(request, 'dashboard/dashboard.html', context)

    # 2. Customer Dashboard (Personal Data)
    else:
        try:
            customer = request.user.customer_profile
            context = {
                'is_mechanic': False,
                'customer': customer,
                'services': customer.service_records.all().order_by('-date'),
                'wheel_services': (
                    customer.wheel_services.all().order_by('-date')
                ),
            }
        except AttributeError:
            # Handle case where user is logged in but doesn't have a profile
            # yet
            context = {'is_mechanic': False, 'no_profile': True}

        return render(request, 'dashboard/customer_dashboard.html', context)
