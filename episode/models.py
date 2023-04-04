from django.db import models


class Season(models.Model):
    title = models.CharField(max_length=225)
    season_id = models.CharField(max_length=225)

    def __str__(self):
        return self.season_id


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Podcast(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='podcasts')
    author = models.ForeignKey('profile.Profile', on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audios/', null=True, blank=True)
    audio_link = models.CharField(max_length=225, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('profile.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=225, null=True, blank=True)

    # def __str__(self):
    #     if self.author.user.get_full_name():
    #         return f"{self.author.user.get_full_name()}' comment"
    #     return f"{self.author.user.username}' comment"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Like(models.Model):
    author = models.ForeignKey('profile.Profile', on_delete=models.CASCADE)
    music = models.ForeignKey(Podcast, on_delete=models.CASCADE)

