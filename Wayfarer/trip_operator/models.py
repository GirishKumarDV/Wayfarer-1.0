from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

#---
#To create operator
#---
class Operator(models.Model):
    op_name = models.CharField(max_length=100)
    op_phone = models.CharField(max_length=13,unique=True)
    op_email  = models.EmailField(max_length=254)
    op_pass = models.CharField(max_length=254,default=None)
    op_rating = models.CharField(max_length=5)
    trip_count = models.IntegerField(default=0)

    def __str__(self):
        return self.op_name


#---
#To create users in an Organization
#---
class OperatorUser(models.Model):
    operator = models.ForeignKey(Operator,on_delete=models.PROTECT)
    user_name = models.CharField(max_length=100)
    user_pass = models.CharField(max_length=254)
    user_email = models.EmailField(max_length=254)
    user_phone = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.user_name}-{self.operator}'


#---
#Specify category of trip
#---
class Category(models.Model):
    DAY_TREK = "Day Trek"
    TREK_AND_CAMP = "Trekking & Camping"
    NIGHT_TREK = "Night Trek & Camping"
    TOUR = "Tours"
    options = (
        (DAY_TREK,"Day Trek"),
        (TREK_AND_CAMP, "Trekking & Camping"),
        (NIGHT_TREK,"Night Trek & Camping"),
        (TOUR,"Tours"),
    )

    name = models.CharField(max_length=50,choices=options,default=DAY_TREK)

    def __str__(self):
        return self.name

#---
#Trip Table
#---
class Trip(models.Model):

    class TripObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().order_by('location')

    DIFFICULTY_EASY = "Easy"
    DIFFICULTY_EASY_TO_MODERATE = "Easy to Moderate"
    DIFFICULTY_MODERATE = "Moderate"
    DIFFICULTY_MODERATE_TO_HARD = "Moderate to Hard"
    DIFFICULTY_HARD = "Hard"

    options = (
        (DIFFICULTY_EASY,'Easy'),
        (DIFFICULTY_EASY_TO_MODERATE,"Easy to Moderate"),
        (DIFFICULTY_MODERATE_TO_HARD, 'Moderate'),
        (DIFFICULTY_MODERATE_TO_HARD,'Moderate to Hard'),
        (DIFFICULTY_HARD, 'Hard'),
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=Category.DAY_TREK)
    location = models.CharField(max_length=100)
    duration = models.IntegerField()
    avg_rating = models.CharField(max_length=5,default='5')
    operator = models.ForeignKey(Operator,on_delete=models.PROTECT,related_name='trip_operator')
    count = models.IntegerField(default=0)
    total_rating = models.CharField(max_length=10,default='0')
    price = models.CharField(max_length=8)
    difficulty = models.CharField(max_length=100, choices=options, default=DIFFICULTY_EASY_TO_MODERATE)
    objects = models.Manager()
    tripobjects = TripObjects()

    class Meta:
        ordering = ('-avg_rating',)

    def __str__(self):
        return f'{self.location} {self.operator}'

#---
#Gives description of each trip
#---
class TripInstance(models.Model):

    class TripInstanceObjects(models.Manager):
        def get_queryset(self):
            return TripInstance.objects.all()

    options = (
        ('draft','Draft'),
        ('publish','Publish'),
    )

    for_trip = models.ForeignKey(Trip,on_delete=models.PROTECT)
    user = models.ForeignKey(OperatorUser,on_delete=models.PROTECT,default=None)
    created = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # start city
    startpoint = models.CharField(max_length=200)
    pickup_locations = models.TextField(null=True)
    altitude = models.CharField(max_length=10,null=True)
    distance = models.CharField(max_length=10,null=True)
    itinerary = models.TextField(null=True)
    additional_info = models.TextField(null=True)
    rating = models.CharField(max_length=5)
    status = models.CharField(max_length=10,choices=options,default='draft')
    # if true increate count in for_trip.count++ && add rating to total_rating
    is_completed = models.BooleanField(default=False)
    objects = models.Manager()
    tripinstanceobjects = TripInstanceObjects()

    class Meta:
        ordering = ('-start_date',)

    def __str__(self):
        return f'{self.for_trip} {self.startpoint}'



