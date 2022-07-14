from django.contrib import admin
from . import models


class FilterByTitle(admin.SimpleListFilter):
    title = "کلیدهای پر تکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return (
            ("django", "جنگو"),
            ("python", "پایتون"),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains=self.value())


class CommentInLIne(admin.StackedInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "status", "show_image")
    list_editable = ("title",)
    list_filter = ("status", "published", FilterByTitle)
    inlines = (CommentInLIne,)
    search_fields = ("title", "body")


admin.site.register(models.Category)
admin.site.register(models.Comment)
admin.site.register(models.Message)
admin.site.register(models.Like)




