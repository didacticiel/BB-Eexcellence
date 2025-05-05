from typing import Any
from .models import BlockIP
from django.http import HttpResponseForbidden




def block_ip(ip_address):
    BlockIP.objects.get_or_create(ip_address=ip_address)



class BlockIPMiddleware:
    def __init__(self,get_response):
        self.get_response= get_response

    def __call__(self,request):
        ip_adress = request.META["REMOTE_ADDR"]
        if BlockIP.objects.filter(ip_adress=ip_adress).exists():
            return HttpResponseForbidden('Forbidden')
        else:
            return self.get_response(request)
