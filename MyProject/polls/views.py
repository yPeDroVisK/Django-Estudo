from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from .models import Question 
# Create your views here.

# Página inicial
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def details(request, question_id):
    # try:
        # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
        # raise Http404("Questão não existe")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/details.html", {"question": question})

def results(request, question_id):
    response = "Você está olhando os resultados da questão %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Você está votando na questão %s" %question_id)