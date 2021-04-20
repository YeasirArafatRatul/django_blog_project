from django.db import models
from django.urls import reverse
# Create your models here.


class PersonManager(models.Manager):
    def male_persons(self):
        return self.filter(gender='M')
    
 
    def female_persons(self):
        return self.filter(gender='F')


    def total_persons(self):
        return self.all().count()



class Person(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique = True,null=True)
    gender = models.CharField(max_length=6, choices= GENDER,default='N/A')


    # persons = models.Manager()


    #will add our manager here
    objects = PersonManager()
    # males = MaleManager()
    # females = FemaleManager()
    # all_persons = AllPersons()

    class Meta:
        # default_manager_name = "persons"
        verbose_name_plural = 'All Persons'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    #methods
    def get_absolute_url(self):
        """returns the url to access an individual object of the model."""
        return reverse('person-detail-view', kwargs={'pk': self.id})
    


class PersonsProfile(models.Model):
    user = models.OneToOneField(Person,on_delete=models.CASCADE)
    bio = models.CharField(max_length=100,null=True,blank=True)
    phone_no = models.PositiveIntegerField(unique=True,null=True)


    @property
    def username(self):
        return self.user.full_name

    def __str__(self):
        return self.user.full_name







class Car(models.Model):
    owner = models.ManyToManyField(Person)
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.name

