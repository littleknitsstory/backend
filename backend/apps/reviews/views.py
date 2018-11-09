from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .forms import ReviewForm
import datetime

from .models import Review, Product

class ListView(TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.order_by('-pub_date')[:5]
        return context


def add_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        product =form.cleaned_data('product')
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.product = product
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('reviews:review-list'))

    return render(request, 'reviews.html', {'form': form})