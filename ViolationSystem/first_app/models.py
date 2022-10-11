from django.db import models
import re
import datetime

class DriverManager(models.Manager):
     def basic_validator(self, postData):
        errors = {}
        if len(postData['fullname']) < 10:
            errors["fullname"] = "Your name should be at least 10 characters"
        if  str(datetime.date.today())-postData['birthday'] <= 18  :
            errors["last_name"] = "Your Age Must be more than  or equal 18"
        if postData['cpassword']!=postData['password']:
            errors["cpassword"] = "The Password doesnt match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Invalid email format"
        if len(postData['password']) < 8:
            errors["password"] = "The Password should be at least 8 characters"
        PHONE_REGEX=re.compile(r'^05(9[987542]|6[982])\d{6}$')
        if not PHONE_REGEX.match(postData['phonenumber']):
            errors['email'] = "Invalid Number"

        return errors

class Driver(models.Model):
    full_name=models.CharField(max_length=30)
    birthday=models.DateField()
    notional_id=models.IntegerField(null=True)
    city=models.CharField(max_length=30)
    blood_type=models.CharField(max_length=4)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    phone_number=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=DriverManager()


class PoliceManager(models.Manager):
     def basic_validator(self, postData):
        errors = {}
        if len(postData['fullname']) < 10:
            errors["fullname"] = "Your name should be at least 10 characters"
        if postData['cpassword']!=postData['password']:
            errors["cpassword"] = "The Password doesnt match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):            
            errors['email'] = "Invalid email format"
        if len(postData['password']) < 8:
            errors["password"] = "The Password should be at least 8 characters"
        PHONE_REGEX=re.compile(r'^05(9[987542]|6[982])\d{6}$')
        if not PHONE_REGEX.match(postData['phonenumber']):
            errors['email'] = "Invalid Number"
        return errors

class Police(models.Model):
    full_name=models.CharField(max_length=30)
    birthday=models.DateField()
    city=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=20)
    phone_number=models.IntegerField(null=True)
    police_to_driver=models.ManyToManyField(Driver, related_name="drivertopolice")#FK M-M
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Licenses(models.Model):
    relased_date=models.DateField()
    expierd_date=models.DateField()
    vechile_type=models.CharField(max_length=20)
    driver=models.OneToOneField(Driver,on_delete=models.CASCADE)#FK 1-1
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Vechile(models.Model):
    vechile_model=models.CharField(max_length=30)
    vechile_number=models.CharField(max_length=20)
    driver=models.ForeignKey(Driver,related_name="vechiles", on_delete=models.CASCADE)#FK 1 TO M
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Violaion(models.Model):
    location=models.CharField(max_length=60)
    expierd_date=models.DateField(null=True)
    fees=models.IntegerField()
    resson=models.CharField(max_length=255)
    violation_date=models.DateField()
    driver=models.ForeignKey(Driver,related_name="dviolations", on_delete=models.CASCADE)
    police=models.ForeignKey(Police,related_name="pviolations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
