from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm

from .models import Review


class ReviewsListView(ListView):
    model = Review
    template_name = 'reviews/list.html'

    def get_context_data(self, **kwargs):
        context = super(ReviewsListView, self).get_context_data(**kwargs)
        context['reviews'] = Review.objects.all()
        return context


def add_review(request):
    form = ReviewForm(request.POST)
    if form.is_valid():
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.user_name = user_name
        review.comment = comment
        review.save()
        return HttpResponseRedirect(reverse('reviews:review-list'))

    return render(request, 'list.html', {'form': form})
