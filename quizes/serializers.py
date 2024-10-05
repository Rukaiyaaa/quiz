from rest_framework import serializers
from .models import Quiz
from questions.serializers import QuestionSerializer

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, source='get_questions')

    class Meta:
        model = Quiz
        fields = '__all__'
