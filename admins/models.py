from django.db import models

# Create your models here.


class EmplyoyeeDailyTask(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    desc = models.TextField()

    def __str__(self):
        return self.title


class FertilizerStock(models.Model):
    FERTILIZER_TYPE_CHOICES = (
        ('Urea', 'Urea'),
        ('Phosphorus', 'Phosphorus'),
        ('Potassium', 'Potassium'),
        ('Rock Phospate', 'Rock Phospate'),
        ('Nitrogen', 'Nitrogen'),
    )
    fertilizer_type = models.CharField(
        max_length=25, choices=FERTILIZER_TYPE_CHOICES, unique=True)
    stock_units = models.PositiveIntegerField()


class SeedStock(models.Model):
    SEED_TYPE_CHOICES = (
        ('Ground Nuts', 'Ground Nuts'),
        ('Sun Flower', 'Sun Flower'),
        ('Paddy', 'paddy'),
        ('Wheat', 'Wheat'),
        ('Rice', 'Rice'),
    )
    seed_type = models.CharField(
        max_length=25, choices=SEED_TYPE_CHOICES, unique=True)
    stock_units = models.PositiveIntegerField()


class FamersFeedback(models.Model):
    feedback_name = models.CharField(max_length=100)
    feedback_desc = models.TextField()
    farmer_name = models.CharField(max_length=100)
    farmer_user_id = models.CharField(max_length=100)

    def __str__(self):
        return self.feedback_name
