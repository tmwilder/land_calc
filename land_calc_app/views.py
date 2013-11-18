#standard
import json
import sys
from collections import Counter
#django
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
#local
import modules.combinatorics
import modules.density

def main(request):
    return render(request, "main.html")


def get_odds(request):
    if request.is_ajax():
        data = json.loads(request.GET['data'])

        deck_dict = data['deck']
        for key, value in deck_dict.items():
            deck_dict[key] = int(value)
        deck = Counter(deck_dict)

        card_cost = Counter(data['card_cost'])
        for key, value in card_cost.items():
            card_cost[key] = int(value)

        on_the_play = data['on_the_play']

        import pdb; pdb.set_trace()

        probability = modules.density.get_odds_range(
            end_turn=11,
            deck=deck,
            card_cost=card_cost,
            on_the_play=True
        )
        return HttpResponse(json.dumps(probability))
    else:
        raise Http404
