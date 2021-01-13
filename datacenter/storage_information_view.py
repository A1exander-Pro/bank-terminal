from datacenter.models import Passcard
from datacenter.models import Visit, is_visit_long
from datacenter.models import get_format
from django.shortcuts import render



def storage_information_view(request):
    unleaved_visit = Visit.objects.filter(leaved_at=None)

    non_closed_visits = []

    for visits in unleaved_visit:    
        non_closed_visit = {
                "who_entered": visits.passcard.owner_name,
                "entered_at": visits.entered_at,
                "duration": get_format(visits.get_duration()),
                "is_strange": is_visit_long(visits.get_duration(), minutes=60)
            } 
        non_closed_visits.append(non_closed_visit)

    context = {
         "non_closed_visits": non_closed_visits,  # не закрытые посещения
      }
    return render(request, 'storage_information.html', context)