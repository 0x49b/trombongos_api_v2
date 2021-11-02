from django.db import models

DAYS = [
    ("Montag", "Montag",),
    ("Dienstag", "Dienstag",),
    ("Mittwoch", "Mittwoch",),
    ("Donnerstag", "Donnerstag",),
    ("Freitag", "Freitag",),
    ("Samstag", "Samstag",),
    ("Sonntag", "Sonntag",)
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


class Evening(models.Model):
    class Meta:
        verbose_name = "Abend"
        verbose_name_plural = "Abende"
        ordering = ('-date',)

    name = models.CharField(max_length=10, null=False, blank=False, choices=DAYS)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "%s %s" % (self.name, self.date)


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
        ordering = ('-date', 'play')

    name = models.CharField(max_length=512, null=False, blank=False)
    season = models.ForeignKey(Season, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    evening = models.ForeignKey(Evening, on_delete=models.DO_NOTHING)
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

    def __str__(self):
        return self.name
