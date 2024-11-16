from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    public_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('public_date',)