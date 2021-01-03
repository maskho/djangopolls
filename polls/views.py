from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# from django.http import Http404

# from django.template import loader

# Create your views here.


def index(request):
    lts_quest_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": lts_quest_list,
    }
    return render(request, "polls/index.html", context)


def detail(request, quest_id):
    question = get_object_or_404(Question, pk=quest_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, quest_id):
    response = "Anda melihat hasil dari pertanyaan %s"
    return HttpResponse(response % quest_id)


def vote(request, quest_id):
    return HttpResponse("Anda memilih pada pertanyaan %s" % quest_id)
