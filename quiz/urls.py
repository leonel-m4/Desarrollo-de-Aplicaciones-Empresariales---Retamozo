from django.urls import path
from .views import ExamListView, ExamDetailView, QuestionCreateView

urlpatterns = [
    path('', ExamListView.as_view(), name='exam_list'),
    path('<int:pk>/', ExamDetailView.as_view(), name='exam_detail'),
    path('question/new/<int:exam_pk>/', QuestionCreateView.as_view(), name='question_create'),
]