from django.shortcuts import render, redirect
from django.contrib.auth import views
from .models import Hits
from .forms import HitForm
from accounts.models import HitMan, Manager


# Create your views here.


def hits(request):
    return render(request, 'hits/home.html')


def create_hits(request):
    if request.method == 'POST':
        hitForm = HitForm(request.POST)
        hitMan = hitForm['id_hitman'].value()
        current_user = request.user

        current_user = current_user.username
        hitUser = HitMan.objects.get(id=hitMan)
        isActiveHitMan = hitUser.state
        hitUser = hitUser.user
        if isActiveHitMan == 'A':
            if hitUser != current_user:
                if hitForm.is_valid():
                    hit = hitForm.save(commit=False)
                    hit.created_by = current_user
                    hit.save()
                    return redirect('create_hits')
                else:
                    print(hitForm.errors)
            else:
                print(' Can not assign to yourself.')
        else:
            print('Hitman is not active')

    else:
        hitForm = HitForm()
    return render(request, 'hits/create_hits.html', {'hitForm': hitForm})


def showHits(request):
    current_user = request.user
    user_name = current_user.username
    if current_user.is_hitman:
        role = current_user.get_hitman_profile()
        if role:
            hitUser = HitMan.objects.get(user=user_name)
            print(hitUser)
            #histHitman = Hits.objects.filter(id_hitman_id=hitUser.id)
            #hitsListHitman = histHitman.values_list('id', 'description', 'target', 'status', 'created_by')

            print('I am Hitman')
            #print(hitsListHitman)
            render(request, 'hits/home.html')
        else:
            print('Assign the role Hitman')
            render(request, 'hits/home.html')
    else:
        print('Assign a role')
        render(request, 'hits/home.html')


