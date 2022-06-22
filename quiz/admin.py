from pyexpat import model
from turtle import title
from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

@admin.register(models.Quizzes)

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

class AnswerInLineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right',
    ]

@admin.register(models.Question)

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
       ]
    list_displays = [
        'title',
        'quiz',
        'date_updated',
        ]
    inlines = [
        AnswerInLineModel,
       ]

@admin.register(models.Answer)

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]
