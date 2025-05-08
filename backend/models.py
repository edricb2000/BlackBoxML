

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Your existing model (unchanged)
class TrainedModel(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    file = models.FileField(upload_to='models/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (v{self.version})"

# New: User credit system
class UserCredits(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits = models.IntegerField(default=10, validators=[MinValueValidator(0)])

    def deduct_credits(self, amount):
        """Safe credit deduction (prevents negative values)"""
        self.credits = max(0, self.credits - amount)
        self.save()

    def __str__(self):
        return f"{self.user.username}: {self.credits} credits"

# New: Prediction logs (optional)
class PredictionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(TrainedModel, on_delete=models.SET_NULL, null=True)
    input_data = models.JSONField()
    output_data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    credits_used = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} → {self.model.name}"
