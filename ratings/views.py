from django.http import HttpResponse
from scripts import actorator


def get_rating(request, actor_name):
    try:
        actor_score = actorator.find_full_actor_score(actor_name)
        return HttpResponse(str(actor_score))
    except:
        return HttpResponse(actor_name)
