from dataclasses import fields
import imp
from pyexpat import model
from turtle import title
from rest_framework import serializers

import quiz
from .models import Quizzes, Question, Answer


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quizzes
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:

        model = Answer
        fields = [
            'id',
            'answerr_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True )
    class Meta:
        model = Question
        fields = [
            'title','answer',
        ]

class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True )
    quiz = QuizSerializer(read_only=True )
    class Meta:
        model = Question
        fields = [
           'quiz', 'title','answer',
        ]