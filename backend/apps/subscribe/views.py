from django.shortcuts import render
from django.views import View
from .forms import SubscribeForm


class ViewSubscribe(View):
    form_class = SubscribeForm
    initial = {'key': 'value'}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        if request.GET.get('email'):
            form = self.form_class(request.GET)
            if form.is_valid():
                form.save()
                return render(request, 'subscribe/success_subscribe.html')
        return render(request, 'components/_sidebar.html', {'form': form})

