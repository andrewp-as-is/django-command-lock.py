from django.db import models

class Command(models.Model):
    app = models.CharField(max_length=255,null=True,blank=True)
    name = models.CharField(unique=True,max_length=255)
    is_locked = models.BooleanField(default=True,verbose_name='locked')
    pid = models.IntegerField()

    class Meta:
        db_table = 'django_command_lock'
        indexes = [
           models.Index(fields=['app',]),
           models.Index(fields=['name',]),
           models.Index(fields=['is_locked',]),
        ]
        ordering = ('app','name',)
        unique_together = [['app','name',]]
