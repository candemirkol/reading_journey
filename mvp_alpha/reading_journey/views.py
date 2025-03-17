from django.db.models import Exists, OuterRef
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Journey, Archipelago, Island, LessonCompletion


def index(request):
    journeys = Journey.objects.all()
    return render(request, 'reading_journey/index.html', {'journeys': journeys})

def archipelago_detail(request, archipelago_id):
    archipelago = get_object_or_404(Archipelago, id=archipelago_id)
    user = request.user

    # Annotate islands with completion status
    islands = Island.objects.filter(archipelago=archipelago).annotate(
        completed=Exists(LessonCompletion.objects.filter(
            user=user,
            island=OuterRef('pk')
        ))
    )

    context = {
        'archipelago': archipelago,
        'islands_with_status': islands
    }

    return render(request, 'reading_journey/archipelago_detail.html', context)

@login_required
def island_detail(request, island_id):
    island = get_object_or_404(Island, pk=island_id)

    # User island completion check
    completed = LessonCompletion.objects.filter(user=request.user, island=island).exists()

    # Completion action handling
    if request.method == 'POST':
        if not completed:
            LessonCompletion.objects.create(user=request.user, island=island)
        return redirect('reading_journey:archipelago_detail', archipelago_id=island.archipelago.id)
    
    return render(request, 'reading_journey/island_detail.html', {'island': island, 'completed': completed})

