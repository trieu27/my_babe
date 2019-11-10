from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .trymore.text_classification.short_text_classifiers import test
@csrf_exempt
def intent(request):
    if request.method == 'POST':
        content = json.loads(request.body.decode('utf-8'))
        content = content["Content"]
        result =  test(content)
#        result =  test(content)
#        content = request.POST['content'];
#        result = findintend(content)
#        
    return JsonResponse({"rs":result}, status=status.HTTP_201_CREATED)

    