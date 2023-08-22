from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView,DetailView

from orderfood.forms import OrderForm
from orderfood.models import Order


class IndexView(TemplateView):
    template_name = "base.html"


class  OrderListView(ListView):
    model = Order
    template_name = "list.html"
    context_object_name = "orders"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status')
        search = self.request.GET.get('search')
        order_id = self.request.GET.get('order_id')

        if search:
            queryset = queryset.filter(
                Q(total_price__contains = search)
            )
        if status:
            queryset = queryset.filter(
                status=status
            )
        if order_id:
            queryset = queryset.filter(
                order_id = order_id
            )
        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all()
        context["search"] = self.request.GET.get("search","")
        order_id = self.request.GET.get("order_id","")
        context["status"] = self.request.GET.get("status")

        if order_id:
            order_id = int(order_id)
        else:
            order_id = 0
        context["order_id"] = order_id
        return context

class  OrderCreateView(CreateView):
    model = Order
    form_class =OrderForm
    template_name = "form.html"
    success_url = "order/list"

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = "form.html"
    success_url = "order/list"

class OrderDetailView(DetailView):
    model = Order

