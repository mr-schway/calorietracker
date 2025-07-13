from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Food(models.Model):
  name = models.CharField(max_length=100)
  carbs = models.FloatField()
  protein = models.FloatField()
  fats = models.FloatField()
  calories = models.IntegerField()

  def __str__(self):
    return self.name
  
class Consume(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  consumedFood = models.ForeignKey(Food, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user} --> {self.consumedFood}"
  


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    calorieGoal = models.IntegerField(default=2000)

    def __str__(self):
      return f"{self.user.username}'s Profile"

# Auto-create profile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user=instance)