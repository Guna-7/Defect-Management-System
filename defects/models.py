from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DeveloperData(models.Model):
    dev_name = models.ForeignKey(User,on_delete=models.CASCADE)
    designation = models.CharField(max_length=200)
    experience = models.PositiveIntegerField()

    def __str__(self):
        return self.dev_name.username

class TesterData(models.Model):
    tester_name = models.ForeignKey(User,on_delete=models.CASCADE)
    designation = models.CharField(max_length=300)
    experience = models.PositiveIntegerField()
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.tester_name.username

class defectData(models.Model):
    defect_id = models.CharField(max_length=100)
    defect_name = models.CharField(max_length=250)
    assigned_date = models.DateField(auto_now_add=True)
    assigned_by = models.ForeignKey(TesterData,on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(DeveloperData,on_delete=models.CASCADE)
    priority = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    defect_status = models.CharField(max_length=100)

    def __str__(self):
        return self.defect_name
    

class Defect_Screenshot(models.Model):
    defect = models.ForeignKey(defectData,on_delete=models.CASCADE)
    defect_img = models.ImageField(upload_to='defectsimg',null=True,blank=True)

    # def __str__(self):
    #     return self.defect