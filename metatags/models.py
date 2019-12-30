from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _


class MetaTag(models.Model):
    url = models.CharField(_('URL-path'), max_length=100, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey()
    title = models.CharField(_('title'), max_length=80, blank=True)
    keywords = models.CharField(_('keywords'), max_length=250, blank=True)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        ordering = ('id',)
        db_table = 'meta_tags'
        unique_together = ('content_type', 'object_id')
        verbose_name = _('meta tags')
        verbose_name_plural = _('meta tags')

    def __str__(self):
        if self.content_object:
            return force_str(self.content_object)
        return self.title
