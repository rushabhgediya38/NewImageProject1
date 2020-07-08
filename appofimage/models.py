from django.db import models

# Create your models here.


class category(models.Model):
    cat_title = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.cat_title


class post(models.Model):
    cat = models.ForeignKey(category, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=500, default="")
    post_dec = models.TextField()
    post_date = models.DateTimeField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.post_title
