from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Comments(models.Model):
    comment = models.TextField()
    authur = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.authur.username + "  is commented."

class AcademicDetails(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateField()
    content = models.TextField(blank=True)
    file = models.FileField(upload_to="academicdocs/")
    authur = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " "+self.authur.username
    
class WorkProcess(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='workdocs/',blank=True)
    authur = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comments,blank=True)        

    def __str__(self):
        return self.title + " "+ self.authur.username + str(self.pub_date) 