from django.contrib import admin
from .models import Exam, Question, Choice

# Register your models here.

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "Examen"
        verbose_name_plural = "Exámenes"

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ["enunciado"]
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    class Meta:
        ordering = ["texto"]
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"
