from django.db import models

from django.db import models

class Cardetail(models.Model):
    carmodel = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)

    TRANSMITION = [
        ('Mannual','Mannual'),
        ('Automatic','Automatic'),
    ]
    transmition = models.CharField(max_length=10,choices=TRANSMITION)

    ENGINE_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Ev', 'Ev'),
    ]
    engine = models.CharField(max_length=10, choices=ENGINE_CHOICES)
    
    rent = models.IntegerField()  # Removed max_length, as it's not supported for IntegerField
    
    LOCATION_CHOICES = [
        ("Alappuzha", "Alappuzha"),
        ("Ernakulam", "Ernakulam"),
        ("Idukki", "Idukki"),
        ("Kannur", "Kannur"),
        ("Kasaragod", "Kasaragod"),
        ("Kollam", "Kollam"),
        ("Kottayam", "Kottayam"),
        ("Kozhikode", "Kozhikode"),
        ("Malappuram", "Malappuram"),
        ("Palakkad", "Palakkad"),
        ("Pathanamthitta", "Pathanamthitta"),
        ("Thiruvananthapuram", "Thiruvananthapuram"),
        ("Thrissur", "Thrissur"),
        ("Wayanad", "Wayanad"),
    ]

    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)


    image = models.ImageField(upload_to="cars/images",null=True,blank=True)
    discription = models.CharField(max_length=200)

    def __str__(self):
        return self.carmodel 
    



class Maketrip(models.Model):
    pickup = models.CharField(max_length=50)
    dropoff = models.CharField(max_length=50)
    pick_date = models.CharField(max_length=30)
    drop_date = models.CharField(max_length=30)
    time = models.CharField(max_length=30)