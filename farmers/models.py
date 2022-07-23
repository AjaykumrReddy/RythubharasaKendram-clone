from django.db import models

# Create your models here.


class FarmerRegistrationModel(models.Model):
    name = models.CharField(max_length=120)
    user_id = models.CharField(unique=True, max_length=120)
    password = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=120)
    aadhar_no = models.CharField(unique=True, max_length=120)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'FarmerRegistration'


class SoilTestSlotBookingModel(models.Model):
    SOIL_TYPE_CHOICES = (
        ('Red-soil', 'Red soil'),
        ('Black-soil', 'Black soil'),
        ('Deltaic-alluvial-soil', 'Deltaic alluvial soil'),
        ('Coastal-alluvial-soil', 'Coastal alluvial soil'),
        ('Laterite-soil', 'Laterite soil'),
        ('Skeletal-Soil', 'Skeletal Soil')
    )
    STATUS_CHOICES = (
        ('placed', 'placed'),
        ('processed', 'processed'),
        ('accepted', 'accepted'),
        ('slotAlloted', 'slotAlloted'),
        ('result', 'result')
    )
    name = models.CharField(max_length=120)
    user_id = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)
    survey_no = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=120)
    soil_type = models.CharField(max_length=25, choices=SOIL_TYPE_CHOICES)
    address = models.CharField(max_length=120)
    tracking_id = models.CharField(max_length=16, unique=True)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=120, default='placed', choices=STATUS_CHOICES)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'SoilTestSlotBooking'


class SeedsOrderingModel(models.Model):
    SEED_TYPE_CHOICES = (
        ('Ground Nuts', 'Ground Nuts'),
        ('Sun Flower', 'Sun Flower'),
        ('Paddy', 'paddy'),
        ('Wheat', 'Wheat'),
        ('Rice', 'Rice'),
    )
    STATUS_CHOICES = (
        ('placed', 'placed'),
        ('processed', 'processed'),
        ('pickedUp', 'pickedUp'),
        ('shipped', 'shipped'),
        ('outOfDelivery', 'outOfDelivery'),
        ('delivered', 'delivered')
    )
    name = models.CharField(max_length=120)
    user_id = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)
    survey_no = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=120)
    seed_type = models.CharField(max_length=25, choices=SEED_TYPE_CHOICES)
    no_of_packets = models.PositiveIntegerField()
    address = models.CharField(max_length=120)
    tracking_id = models.CharField(max_length=16, unique=True)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=120, default='placed', choices=STATUS_CHOICES)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'SeedsOrdering'


class FertilizersOrderingModel(models.Model):
    FERTILIZER_TYPE_CHOICES = (
        ('Urea', 'Urea'),
        ('Phosphorus', 'Phosphorus'),
        ('Potassium', 'Potassium'),
        ('Rock Phospate', 'Rock Phospate'),
        ('Nitrogen', 'Nitrogen'),
    )
    STATUS_CHOICES = (
        ('placed', 'placed'),
        ('processed', 'processed'),
        ('pickedUp', 'pickedUp'),
        ('shipped', 'shipped'),
        ('outOfDelivery', 'outOfDelivery'),
        ('delivered', 'delivered')
    )
    name = models.CharField(max_length=120)
    user_id = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)
    survey_no = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=120)
    fertilizer_type = models.CharField(
        max_length=25, choices=FERTILIZER_TYPE_CHOICES)
    no_of_packets = models.PositiveIntegerField()
    address = models.CharField(max_length=120)
    tracking_id = models.CharField(max_length=16, unique=True)
    date = models.DateTimeField()
    status = models.CharField(
        max_length=120, default='placed', choices=STATUS_CHOICES)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = 'FertilizersOrdering'
