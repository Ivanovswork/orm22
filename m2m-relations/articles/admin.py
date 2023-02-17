from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope



class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        c = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data['is_main']:
                c += 1
        if c != 1:
            raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = []


@admin.register(Scope)
class ScopesAdmin(admin.ModelAdmin):
    list_display = ["id", "tag", "article", "is_main"]
    inlines = []