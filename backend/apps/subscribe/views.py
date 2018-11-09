from django.views import View
from .forms import SubscribeForm
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

class SuccessSubscribe(TemplateView):
    template_name = 'subscribe/success_subscribe.html'


class AjaxSubscribe(View):
    def post(self, request):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            url = reverse_lazy('subscribe:success_subscribe')
            form.save()
            response_dict = {'response': 'success', 'url': url}
            return JsonResponse(response_dict)
        response_dict = {'response': 'Вы уже подписаны.'}
        return JsonResponse(response_dict)


