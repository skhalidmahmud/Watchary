from django.db import models

# Create Movie models.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.ImageField(upload_to="static/")
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    age_rating = models.CharField(max_length=5)
    duration = models.IntegerField(help_text="Duration in minutes")
    director = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.title} ({self.release_year})"
    

# Create TVSeries models.

class TVSeries(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    age_rating = models.CharField(max_length=5)
    seasons = models.IntegerField(default=1)
    director = models.CharField(max_length=100)
    is_ongoing = models.BooleanField(default=True)
    
    def __str__(self):
        status = "Ongoing" if self.is_ongoing else "Completed"
        return f"{self.title} ({self.release_year}, {status})"

class Episode(models.Model):
    series = models.ForeignKey(TVSeries, on_delete=models.CASCADE, related_name='episodes')
    season_number = models.IntegerField()
    episode_number = models.IntegerField()
    title = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in minutes")
    air_date = models.DateField()
    
    class Meta:
        ordering = ['season_number', 'episode_number']
        unique_together = ['series', 'season_number', 'episode_number']
    
    def __str__(self):
        return f"{self.series.title} S{self.season_number}E{self.episode_number}: {self.title}"