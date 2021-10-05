from django.views import View
from django.http.response import JsonResponse
from django.views.decorators.http import require_http_methods
from doges.models import Breed
import json

class BreedView(View):
  
  http_method_names = ['get', 'post']

  def get(self, request, *args, **kwargs):
    return JsonResponse({'message':'Created'}, status=200)

  def post(self, request, *args, **kwargs):
    if not request.body:
      return JsonResponse({'message':'Missing body'}, status=400)
    data=json.loads(request.body)
    name = ''
    if not 'name' in data:
      return JsonResponse({'message':'Missing name field'}, status=400)
    name = data['name']
    br = Breed(name=name)
    br.save()
    return JsonResponse({'message':'Created'}, status=201)