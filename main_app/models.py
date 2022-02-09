from django.db import models


class Print(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.IntegerField(default=0)
    price = models.TextField(max_length=500)
    verified_print = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']