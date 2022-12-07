from time import time

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class AjaxHandlerView(View):
    def get(self, request):
        text = request.GET.get('button_text')
        is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax:
            return JsonResponse({'seconds': time()})
        return render(request, 'app/index.html')

    def post(self, request):
        card_text = request.POST.get('text')
        result = f'Eu tenho {card_text}'
        return JsonResponse({'data': result})
