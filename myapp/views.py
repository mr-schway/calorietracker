from django.shortcuts import render

from myapp.models import Consume, Food

# Create your views here.
def index(request):
  if request.method == "POST":
    # consumedFood = request.POST['consumedFood']
    consumedFoodName = request.POST.get('consumedFood', '') # or this
    food = Food.objects.get(name = consumedFoodName)
    user = request.user
    consume = Consume(consumedFood = food, user = user)
    consume.save()
  foods = Food.objects.all()
  return render(request, 'myapp/index.html', {'foods': foods})