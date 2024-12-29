from django.db import models

class OurService(models.Model):
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='service/', blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Service ID {self.id} - {self.title}"

class OurProject(models.Model):
    STATUS = (
        ('Running', 'Running'),
        ('Complete', 'Complete'),
        ('Stop', 'Stop'),
    )
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='project/', blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS, default="Running", max_length=20)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return f"Project ID {self.id} - {self.title}"


class OurTeam(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    designation = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.id} - {self.name}"
    
class CompanyInformation(models.Model):
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    cover = models.ImageField(upload_to='company/', blank=True, null=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=600, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)

