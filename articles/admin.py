from django.contrib import admin
from .models import Article, Tag, ArticleTag
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ArticleTagInlineFormset(BaseInlineFormSet):

    def clean(self):
        checked = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                checked += 1
        if checked > 1:
            raise ValidationError('Основным может быть только один раздел')
        elif checked == 0:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

