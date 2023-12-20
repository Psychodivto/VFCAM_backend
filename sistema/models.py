from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

from django.dispatch import receiver


# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='foto_perfil', blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    google_id = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):

        if created:
            Userprofile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):

        instance.userprofile.save()


class Question(models.Model):
    nombre = models.CharField(max_length=200)
    anios = models.IntegerField(default=0)
    peso = models.IntegerField(default=0)
    imc = models.IntegerField(default=0)
    objetivo = models.CharField(max_length=200)
    cuentame = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
