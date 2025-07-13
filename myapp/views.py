from django.shortcuts import render
from myapp.models import Consume, Food, UserProfile

def index(request):
  if request.method == "POST":
      form_type = request.POST.get('form_type')
      user = request.user

      if form_type == 'add_food':
        consumedFoodName = request.POST.get('consumedFood', '')
        if consumedFoodName:
          try:
            food = Food.objects.get(name=consumedFoodName)
            Consume.objects.create(consumedFood=food, user=user)
          except Food.DoesNotExist:
            pass  # Or handle with a message

      elif form_type == 'set_goal':
        calorieGoal = int(request.POST.get('calorieGoal', 0))
        if calorieGoal > 0:
          UserProfile.objects.update_or_create(
             user=user,
             defaults={'calorieGoal': calorieGoal}
            )

  foods = Food.objects.all()
  consumedFoodsUser = Consume.objects.filter(user=request.user)
  profile, _ = UserProfile.objects.get_or_create(user=request.user)
  calorieGoal = profile.calorieGoal

  return render(request, 'myapp/index.html', {
    'foods': foods,
    'consumedFoodsUser': consumedFoodsUser,
    'calorieGoal': calorieGoal
  })