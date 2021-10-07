from django.db import models


class SingletonModel(models.Model):
    """Singleton abstract base model."""

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class TimeStampedModel(models.Model):
    """Time stamped abstract base model."""

    modified = models.DateTimeField(auto_now=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        abstract = True
