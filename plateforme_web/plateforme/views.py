from django.http import HttpResponse
from .models import Test

def index(request):

    test =Test.objects.create()


    return HttpResponse(test.id)
