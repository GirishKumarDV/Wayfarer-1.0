from django.db import models
from django.contrib.auth.models import User
from trip_operator.models import TripInstance
from django.utils import timezone
from django.contrib.auth.hashers import make_password



class Nomad(models.Model):
    
    nomad_name = models.CharField(max_length=254)
    nomad_email = models.EmailField(max_length=254)
    nomad_phone = models.CharField(max_length=13)
    nomad_pass = models.CharField(max_length=100)
    nomad_dp = models.ImageField(default=None,upload_to='nomad-dps/')
    nomad_objects = models.Manager()

    def save(self,*args,**kwargs):
        self.nomad_pass = make_password(self.nomad_pass)
        super(Nomad,self).save(*args,**kwargs)

    def __str__(self):
        return self.nomad_name
    
class Booking(models.Model):
    class BookingObjects(models.Manager):
        def get_queryset(self):
            return Booking.objects.all()
    nomad = models.ForeignKey(Nomad,on_delete=models.PROTECT)
    for_trip = models.ForeignKey(TripInstance,on_delete=models.PROTECT)
    booking_date = models.DateField(default=timezone.now)
    cancelled = models.BooleanField(default=False)
    booking_amount = models.DecimalField(max_digits=15,decimal_places=4)
    participant_count = models.IntegerField(default=1)
    participants = models.TextField(null=True)
    trek_rating = models.FloatField()
    organizer_rating = models.FloatField()

    bookingobjects = BookingObjects()
    objects = models.Manager()

    class Meta:
        ordering = ('-booking_date',)

    def __str__(self):
        return f'{self.nomad.nomad_name} {self.for_trip.for_trip.location}'
