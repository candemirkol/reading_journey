from django.db import models


class Journey(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Archipelago(models.Model):
    name = models.CharField(max_length=100)
    journey = models.ForeignKey(Journey, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Island(models.Model):
    name = models.CharField(max_length=100)
    archipelago = models.ForeignKey(Archipelago, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.archipelago.name} - {self.name}"

class LessonCompletion(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    island = models.ForeignKey(Island, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.island.name}"
    


"""
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=200)

"""
