from django.db import models


class Exam(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-fecha_creacion"]
        verbose_name = "Examen"
        verbose_name_plural = "Exámenes"

    def __str__(self):
        return self.titulo


class Question(models.Model):
    DIFICULTA_CHOICES = [
        ('FACIL', 'Fácil'),
        ('MEDIUM', 'Medium'),
        ('DIFICIL', 'Difícil'),
    ]
    
    enunciado = models.CharField(max_length=500)
    examen = models.ForeignKey(Exam, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=1)
    dificultad = models.CharField(max_length=100, choices=DIFICULTA_CHOICES, default='MEDIUM')

    class Meta:
        ordering = ["enunciado"]
        verbose_name = "Pregunta"
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.enunciado


class Choice(models.Model):
    texto = models.CharField(max_length=300)
    es_correcta = models.BooleanField(default=False)
    pregunta = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        ordering = ["texto"]
        verbose_name = "Opción"
        verbose_name_plural = "Opciones"

    def __str__(self):
        return self.texto