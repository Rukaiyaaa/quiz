from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, AnswerViewSet

router = DefaultRouter() # amader router

router.register('question', QuestionViewSet) 
router.register('answer', AnswerViewSet) 

 
urlpatterns = [
    path('', include(router.urls)),
]