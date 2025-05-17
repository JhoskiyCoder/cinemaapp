from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    age_limit = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    hall = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.movie.title} - {self.date} {self.time}"

class Viewer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.viewer.name} - {self.session}"
