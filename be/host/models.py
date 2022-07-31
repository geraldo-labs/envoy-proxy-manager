from django.db import models

class Host(models.Model):
    id = models.UUIDField()
    name = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length=255, blank=True, null=True)
    description = models.CharField(default="", null=True, blank=True, max_length=255)

    created = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    updated = models.DateTimeField(auto_now=False, blank=True, null=True)


    class Meta:
        verbose_name = "Host"
        verbose_name_plural = "Hosts"
        app_label = 'host'

    def __str__(self):
        return self.name
