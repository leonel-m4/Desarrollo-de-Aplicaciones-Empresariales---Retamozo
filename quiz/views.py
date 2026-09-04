from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect
from django.forms import inlineformset_factory
from .models import Exam, Question, Choice
from .forms import QuestionForm, ChoiceFormSetWithValidation


class ExamListView(ListView):
    model = Exam
    ordering = ["-fecha_creacion"]
    template_name = "quiz/exam_list.html"


class ExamDetailView(DetailView):
    model = Exam
    template_name_suffix = "_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = self.object.question_set.all()
        return context


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "quiz/question_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.pk:
            context["formset"] = ChoiceFormSetWithValidation(instance=self.object)
        else:
            context["formset"] = ChoiceFormSetWithValidation()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect("exam_detail", pk=self.object.examen.pk)
        return self.form_invalid(form)