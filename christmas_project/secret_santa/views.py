from django.shortcuts import render, redirect
from datetime import date
from .models import Participant
import random
from django.shortcuts import get_object_or_404

def is_it_christmas(request):
    today = date.today()
    is_christmas_message = "Yes!" if today.month == 12 and today.day == 25 else "No!"
    return render(request, 'secret_santa/index.html', {'is_christmas_message': is_christmas_message})


def secret_santa(request):
    participants = Participant.objects.all()
    return render(request, 'secret_santa/secret_santa.html', {'participants': participants})

def add_participant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Participant.objects.create(name=name)
    return redirect('secret_santa')

def randomize_pairs(request):
    participants = list(Participant.objects.all())
    if len(participants) < 2:
        return render(request, 'secret_santa/error.html', {'message': "Not enough participants."})
    
    random.shuffle(participants)
    pairs = [(participants[i], participants[(i + 1) % len(participants)]) for i in range(len(participants))]
    
    return render(request, 'secret_santa/pairs.html', {'pairs': pairs})

def delete_participant(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    participant.delete()
    return redirect('secret_santa')