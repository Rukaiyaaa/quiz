from rest_framework import serializers
from .models import Quiz
from questions.serializers import QuestionSerializer
from category.serializers import CategorySerializer

class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, source='get_questions')

    topic = CategorySerializer()

    class Meta:
        model = Quiz
        fields = '__all__'
