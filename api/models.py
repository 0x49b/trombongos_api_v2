from django.db import models
import uuid

DAYS = [
    ("Montag", "Montag",),
    ("Dienstag", "Dienstag",),
    ("Mittwoch", "Mittwoch",),
    ("Donnerstag", "Donnerstag",),
    ("Freitag", "Freitag",),
    ("Samstag", "Samstag",),
    ("Sonntag", "Sonntag",)
]

CERT = [
    (0, "2G+"),
    (1, "2G"),
    (2, "3G"),
    (3, "3G+"),
]

REGISTER = [
    (0, "Gesamt"),
    (1, "Bläser"),
    (2, "Schläger")
]


class Season(models.Model):
    class Meta:
        verbose_name = "Saison"
        verbose_name_plural = "Saisons"

    name = models.CharField(max_length=9, null=False, blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = "Kategorie"
        verbose_name_plural = "Kategorien"
        ordering = ('sort',)

    name = models.CharField(max_length=512, blank=False, null=False)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Transport(models.Model):
    class Meta:
        verbose_name = "Transport"
        verbose_name_plural = "Transporte"
        ordering = ("id",)

    name = models.CharField(max_length=156, null=False, blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ('date', 'sort')

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512, null=False, blank=False)
    day = models.CharField(max_length=10, null=False, blank=False, choices=DAYS)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    date = models.DateField()
    transport = models.ForeignKey(Transport, on_delete=models.DO_NOTHING)
    ca_makeup = models.BooleanField(default=False)
    makeup = models.TimeField(null=True, blank=True)
    warehouse = models.TimeField(null=True, blank=True)
    sun = models.TimeField(null=True, blank=True)
    gathering = models.TimeField(null=False)
    ca_play = models.BooleanField(default=False)
    play = models.TimeField(null=False)
    trailer = models.CharField(max_length=256, null=True, blank=True)
    information = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    fix = models.BooleanField(default=True)
    cert = models.IntegerField(choices=CERT, default=None, null=True, blank=True)
    sort = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.uuid is None:
            self.uuid = uuid.uuid4()
        super(Event, self).save(*args, **kwargs)


class Calendar(models.Model):
    class Meta:
        verbose_name = "Kalender"
        verbose_name_plural = "Kalender"
        ordering = ('season', 'from_date', 'from_time')

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024, null=False, blank=False)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    register = models.IntegerField(choices=REGISTER, default=0)
    from_date = models.DateField(null=False, blank=False)
    until_date = models.DateField(null=True, blank=True)
    from_time = models.TimeField(null=True, blank=True, verbose_name="From")
    until_time = models.TimeField(null=True, blank=True, verbose_name="Until")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
