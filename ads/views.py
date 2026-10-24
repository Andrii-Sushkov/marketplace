from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Ad, Cart, CartItem
from django.db.models import Q
from django.urls import reverse_lazy

class AdListView(LoginRequiredMixin, ListView):
    model = Ad
    template_name = 'ad_list.html'
    context_object_name = 'ads'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        return queryset        

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    fields = ['title', 'detail', 'image', 'price']
    template_name = 'create_ad.html'
    success_url = reverse_lazy('ad_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    fields = "__all__"
    template_name = 'update_ad.html'
    success_url = reverse_lazy('ad_list')

    def test_func(self):
        ad = self.get_object()
        return ad.author == self.request.user

class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    template_name = 'delete_ad.html'
    success_url = reverse_lazy('ad_list')

    def test_func(self):
        ad = self.get_object()
        return ad.author == self.request.user

class AdDetailView(LoginRequiredMixin, DetailView):
    model = Ad
    template_name = 'ad_details.html'
    context_object_name = 'ad'

class CartListView(ListView):
    model = Cart
    template_name = 'cart_list.html'
    context_object_name = 'cart'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CartItemCreateView(CreateView):
    model = CartItem
    fields = ['quantity ']
    template_name = 'cart_add.html'
    success_url = reverse_lazy('cart_list')

class CartItemDeleteView(DeleteView):
    model = CartItem
    template_name = 'cart_delete.html'
    success_url = reverse_lazy('ad_list')