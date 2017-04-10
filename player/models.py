from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Player(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )

    STATUS_CHOICES = (
        ('UP','Unregistered Player'),
        ('FA','Free Agent'),
        ('AP','Assigned Player'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    primary_phone = models.CharField(max_length=13)
    secondary_phone = models.CharField(max_length=13, blank=True)
    birth_date = models.DateField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    bio = models.TextField(max_length=500, blank=True)

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()