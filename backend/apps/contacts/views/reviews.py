from django.views.generic import ListView, CreateView
from apps.contacts.forms.reviews import ReviewForm
from apps.contacts.models import Review
from django.urls import reverse_lazy


class ReviewsListView(ListView):
    model = Review
    template_name = 'contacts/review-list.html'


class CreateReview(CreateView):
    model = Review
    # fields = [
    #     'user_name', 'email', 'comment'
    # ]
    form_class = ReviewForm
    template_name = 'contacts/review-form.html'
    success_url = reverse_lazy('reviews:review-list')
