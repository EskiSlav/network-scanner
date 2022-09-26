from django.db import models

class Messages(models.Model):
    message_id = models.BigIntegerField(unique=True)
    text = models.TextField()
    user = models.ForeignKey('Users', models.DO_NOTHING, to_field='tg_id')
    direction = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'messages'


class Users(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    is_bot = models.BooleanField(blank=True, null=True)
    username = models.CharField(max_length=128, blank=True, null=True)
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'