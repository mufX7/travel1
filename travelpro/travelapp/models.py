from django.db import models


class place(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()



class team(models.Model):
    def __str__(self):
        return self.name2
    name2=models.CharField(max_length=250)
    img2 = models.ImageField(upload_to='pics2')
    desc2 = models.TextField()


