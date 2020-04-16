from django.contrib import admin
from .models import Question , Choice
# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    
    

