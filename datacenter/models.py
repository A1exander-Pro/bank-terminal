from django.db import models
import django
import datetime
import time


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(self):
        entered_time = django.utils.timezone.localtime(self.entered_at)
        now = django.utils.timezone.localtime()
        leaved_at = django.utils.timezone.localtime(self.leaved_at) if self.leaved_at else now
        delta = leaved_at - entered_time
        return delta.total_seconds()
        

def get_format(unformat_time):
    hour = int(unformat_time // 3600)
    minute = int((unformat_time % 3600)/60)
    return f'{hour}ч:{minute}м'

def is_visit_long(visit, minutes=15):
    minutes_of_visit = visit/60
    result = minutes_of_visit >= minutes
    return result
    