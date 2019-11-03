from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from rest_framework.views import APIView

from .models import Choice, Question


class IndexView(APIView):

    def get(self, request):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        questions = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5].values()
        return JsonResponse({"questions": list(questions)})


class DetailView(APIView):

    def get(self, request, pk):
        """Excludes any questions that aren't published yet."""
        question = Question.objects.filter(pk=pk, pub_date__lte=timezone.now()).values()
        choices = Choice.objects.filter(question_id=pk, question__pub_date__lte=timezone.now()).values()
        return JsonResponse({"question": list(question), "choices": list(choices)})


class Vote(APIView):

    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.data['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return JsonResponse({
                'question_id': question.id,
                'message': "You didn't select a choice.",
                'status': "error"
            }, status=400)
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return JsonResponse({
                'question_id': question.id,
                'message': "vote received",
                'status': "success"
            }, status=200)
