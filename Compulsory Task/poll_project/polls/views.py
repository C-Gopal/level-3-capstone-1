from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """Welcome page"""
    return render(request, "welcome.html")

def polls(request):
    """Displays latest 5 polls in descending order according to publish date"""
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/poll.html", context)

def detail(request, question_id):
    """Displays the details of a selected poll"""
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    """Displays results for selected poll"""
    question = get_object_or_404(Question, pk = question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    """Allows user to vote on poll options"""
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(
            pk = request.POST["choice"]
        )
    except (KeyError, Choice.DoesNotExist):
        # redisplay the question voting form
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing with POST data
        # this prevents data from being posted twice if a user hits the back button
        return HttpResponseRedirect(
            reverse("polls:results", args=(question_id,))
        )
    
