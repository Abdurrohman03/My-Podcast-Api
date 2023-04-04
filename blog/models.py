from django.db import models
from episode.models import Tag, Category


class Blog(models.Model):
    title = models.CharField(max_length=225)
    image = models.ImageField(upload_to='blogs')
    author = models.ForeignKey('profile.Profile', on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    author = models.ForeignKey('profile.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Blog, on_delete=models.CASCADE)
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



