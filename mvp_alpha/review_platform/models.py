from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title

class Wishlist(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, related_name='wishlisted_by')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"