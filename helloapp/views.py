from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello_json(request):
    return JsonResponse({"Message": "Hello World!"})
def hello_html(request):
    return render(request, "hello.html")