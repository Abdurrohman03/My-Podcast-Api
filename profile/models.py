from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='authors')
    bio = models.TextField()

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    @property
    def full_name(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username


def user_post_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)


post_save.connect(user_post_save, sender=User)
