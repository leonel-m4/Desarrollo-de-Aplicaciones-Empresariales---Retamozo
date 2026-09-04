from django import forms
from django.forms import inlineformset_factory
from .models import Exam, Question, Choice


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['titulo', 'descripcion']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['enunciado', 'puntaje', 'examen']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['texto', 'es_correcta']


ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    fields=['texto', 'es_correcta'],
)


class ChoiceFormSetWithValidation(ChoiceFormSet):
    def clean(self):
        super().clean()
        correcta_count = 0
        for form in self.forms:
            if form.cleaned_data.get('es_correcta'):
                correcta_count += 1
        if correcta_count != 1:
            raise forms.ValidationError("Exactly one choice must be marked as correct.")