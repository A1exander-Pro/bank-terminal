from datacenter.models import Passcard
from datacenter.models import Visit, get_format,is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    
    this_passcard_visits = []

    for visits in all_visits:
        this_passcard_visit = {
                "entered_at": visits.entered_at,
                "duration": get_format(visits.get_duration()),
                "is_strange": is_visit_long(visits.get_duration(), minutes=60),
            }
        this_passcard_visits.append(this_passcard_visit)
        
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
