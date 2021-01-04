from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic

# from django.http import Http404

# from django.template import loader

# Create your views here.


# def index(request):
#     lts_quest_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": lts_quest_list,
#     }
#     return render(request, "polls/index.html", context)


# def detail(request, quest_id):
#     question = get_object_or_404(Question, pk=quest_id)
#     return render(request, "polls/detail.html", {"question": question})


# def results(request, quest_id):
#     question = get_object_or_404(Question, pk=quest_id)
#     return render(request, "polls/result.html", {"question": question})
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"


def vote(request, quest_id):
    question = get_object_or_404(Question, pk=quest_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "Anda belum milih jawaban,",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
