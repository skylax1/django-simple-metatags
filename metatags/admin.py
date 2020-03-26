from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .forms import InlineMetaTagForm, MetaTagForm
from .models import MetaTag


class MetaTagInlineMeta(forms.MediaDefiningClass):

    def __new__(mcs, name, bases, attrs):
        if 'modeltranslation' in settings.INSTALLED_APPS:
            from modeltranslation.admin import TranslationGenericStackedInline
            bases = (TranslationGenericStackedInline,)
        return super().__new__(mcs, name, bases, attrs)


class MetaTagAdminMeta(forms.MediaDefiningClass):

    def __new__(mcs, name, bases, attrs):
        if 'modeltranslation' in settings.INSTALLED_APPS:
            from modeltranslation.admin import TranslationAdmin
            bases = (TranslationAdmin,)
        return super().__new__(mcs, name, bases, attrs)


class MetaTagInline(GenericStackedInline, metaclass=MetaTagInlineMeta):
    model = MetaTag
    extra = 1
    max_num = 1
    can_delete = False
    form = InlineMetaTagForm
    template = 'metatags/admin/edit_inline/stacked.html'


@admin.register(MetaTag)
class MetaTagAdmin(admin.ModelAdmin, metaclass=MetaTagAdminMeta):
    form = MetaTagForm
    list_display = ('url',)
    search_fields = ('url', 'title', 'keywords', 'description')

    def get_queryset(self, request):
        return super().get_queryset(request).attached_to_url_path()
