from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify
# Create your models here.
class profile(models.Model):
    x = {('Lab','Lab'),('Hospital','Hospital'),('Clinic','Clinic') , ('Petiant','Petiant')}
    user = models.ForeignKey(User , on_delete = models.CASCADE , blank=True , null=True)
    frist_name= models.CharField(max_length=10 , blank=True , null=True)
    last_name= models.CharField(max_length=10 , blank=True , null=True)
    phone = models.CharField(max_length=11 , blank=True , null=True)
    age = models.IntegerField(blank=True , null=True)
    address= models.CharField(max_length=30 , blank=True , null=True)
    email= models.EmailField(max_length=30 , blank=True , null=True)
    nationalID= models.IntegerField( blank=True , null=True)
    medicalType = models.TextField(choices= x , default='Petiant')
    
    def __str__(self):
        return str(self.frist_name + self.last_name)
    
class doctor(models.Model):
    sex ={('male','male') , ('female','female')}
    special = {('heart','heart') , ('Counselor' , 'Counselor'),('eras && nose', 'eras && nose')}
    reception = models.OneToOneField(profile , on_delete=models.CASCADE , blank=True , null= True)
    name=models.CharField(max_length=200 , null= True , blank= True)
    about=models.TextField(null= True , blank= True)
    specialist=models.TextField(choices=special , null= True , blank= True)
    location=models.CharField(max_length=20 , null= True , blank= True)
    price=models.FloatField(null= True , blank= True)
    image=models.ImageField(upload_to='photo/profilePic')
    years_of_experience = models.IntegerField(null=True,blank=True)
    gender = models.TextField(choices=sex,null=True,blank=True)
    slug = models.SlugField(max_length=30 , default=slugify(name))
    def __str__(self):
        return str(self.name)
    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.name)
            hasSlug = doctor.objects.filter(slug = slug).exists()
            count = 1
            while hasSlug:
                count += 1
                slug = slugify(self.name) + '-' + str(count)
                hasSlug = doctor.objects.filter(slug = slug).exists()
            self.slug = slug
        super().save(*args , **kwargs)

class clinicPICs(models.Model):
    doctor = models.ForeignKey(doctor , on_delete=models.CASCADE)
    pic  = models.ImageField(upload_to='photo/clincPic')