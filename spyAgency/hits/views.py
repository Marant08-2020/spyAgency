from django.shortcuts import render, redirect
from .models import Hits
from .forms import HitForm
from accounts.models import HitMan, Manager
from django.core.exceptions import PermissionDenied


# Create your views here.


def hits(request):
    return render(request, 'hits/home.html')


def create_hits(request):
    current_user = request.user

    if str(current_user) == "AnonymousUser":
        raise PermissionDenied
    if current_user.is_hitman or current_user.is_boss:
        if current_user.get_manager_profile() or current_user.get_boss_profile():
            if request.method == 'POST':
                hitForm = HitForm(request.POST)
                hitMan = hitForm['id_hitman'].value()
                current_user = request.user

                current_user = current_user.username
                hitUser = HitMan.objects.get(id=hitMan)
                isActiveHitMan = hitUser.state
                hitUser = hitUser.user

                if isActiveHitMan == 'A':
                    if hitUser == current_user:
                        if hitForm.is_valid():
                            hit = hitForm.save(commit=False)
                            hit.created_by = current_user
                            hit.save()
                            return redirect('create_hits')
                        else:
                            print(hitForm.errors)
                    else:
                        message = "Can not assign to yourself"
                        print(' Can not assign to yourself.')
                        return render(request, 'hits/create_hits.html', {'hitForm': hitForm, 'message': message})
                else:
                    print('Hitman is not active')

            else:
                hitForm = HitForm()
                return render(request, 'hits/create_hits.html', {'hitForm': hitForm})
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied


def bulk(request):
    context = {
        'histMan': '',
        'roleH': '',
        'messageH': '',
        'roleM': '',
        'histManager': '',
        'messageM': '',
        'roleB': '',
        'histAll': '',
    }
    current_user = request.user

    if str(current_user) == "AnonymousUser":
        raise PermissionDenied

    user_name = current_user.username
    if current_user.is_hitman:
        roleH = current_user.get_hitman_profile()

        if roleH:

            hitUser = HitMan.objects.filter(user__username=user_name).values('id')
            histHitman = Hits.objects.filter(id_hitman_id=hitUser[0]['id']).exclude(status='C')
            hitsListHitman = histHitman.values_list('id', 'description', 'target', 'status', 'created_by')
            context['histMan'] = hitsListHitman
            context['roleH'] = 'hitman'
            # render(request, 'hits/listahits.html', context)
        else:
            context['messageH'] = 'Assign the role Hitman'
            print('Assign the role Hitman')

    if current_user.is_manager:
        roleM = current_user.get_manager_profile()

        if roleM:

            userId = Manager.objects.filter(user__username=user_name).values('id')
            hitsLacey = HitMan.objects.filter(manager_id=userId[0]['id']).values('id')
            hitsLaceys = []
            context['roleM'] = 'manager'
            for h in hitsLacey:
                histHitmanLacey = Hits.objects.filter(id_hitman_id=h['id']).exclude(status='C')
                hitsListHitmanLacey = histHitmanLacey.values_list('id', 'description',
                                                                  'target', 'status', 'created_by')
                hitsLaceys.append(hitsListHitmanLacey)
            context['histManager'] = hitsLaceys
        else:
            context['messageM'] = 'Assign the role Manager'
            print('Assign the role Manager')

    if current_user.is_boss:
        roleB = current_user.get_boss_profile()

        context['roleB'] = 'boss'
        if roleB:
            context['histAll'] = Hits.objects.order_by('id').exclude(status='C')

    return render(request, 'hits/bulk.html', context)


def showHits(request):

    context = {
        'histMan': '',
        'roleH': '',
        'messageH': '',
        'roleM': '',
        'histManager': '',
        'messageM': '',
        'roleB': '',
        'histAll': '',
    }
    current_user = request.user

    if str(current_user) == "AnonymousUser":
        raise PermissionDenied

    user_name = current_user.username
    if current_user.is_hitman:
        roleH = current_user.get_hitman_profile()

        if roleH:

            hitUser = HitMan.objects.filter(user__username=user_name).values('id')
            histHitman = Hits.objects.filter(id_hitman_id=hitUser[0]['id'])
            hitsListHitman = histHitman.values_list('id', 'description', 'target', 'status', 'created_by')
            context['histMan'] = hitsListHitman
            context['roleH'] = 'hitman'
            # render(request, 'hits/listahits.html', context)
        else:
            context['messageH'] = 'Assign the role Hitman'
            print('Assign the role Hitman')

    if current_user.is_manager:
        roleM = current_user.get_manager_profile()

        if roleM:

            userId = Manager.objects.filter(user__username=user_name).values('id')
            hitsLacey = HitMan.objects.filter(manager_id=userId[0]['id']).values('id')
            hitsLaceys = []
            context['roleM'] = 'manager'
            for h in hitsLacey:
                histHitmanLacey = Hits.objects.filter(id_hitman_id=h['id'])
                hitsListHitmanLacey = histHitmanLacey.values_list('id', 'description',
                                                                  'target', 'status', 'created_by')
                hitsLaceys.append(hitsListHitmanLacey)
            context['histManager'] = hitsLaceys
        else:
            context['messageM'] = 'Assign the role Manager'
            print('Assign the role Manager')

    if current_user.is_boss:
        roleB = current_user.get_boss_profile()

        context['roleB'] = 'boss'
        if roleB:
            context['histAll'] = Hits.objects.order_by('id')

    return render(request, 'hits/listahits.html', context)


def detailsHits(request, _id):
    current_user = request.user
    if str(current_user) == "AnonymousUser":
        raise PermissionDenied()

    hitDetail = Hits.objects.get(pk=_id)
    return render(request, 'hits/details.html', {'hitDetail': hitDetail})


def UpdateHits(request, _id):
    current_user = request.user
    #print(current_user)
    if str(current_user) == "AnonymousUser":
        raise PermissionDenied()

    hitUpdate = Hits.objects.get(pk=_id)
    statusHit = hitUpdate.status

    if request.method == 'POST':

        HitFormU = HitForm(request.POST, instance=hitUpdate)

        if current_user.is_hitman and not current_user.is_boss and not current_user.is_manager:
            roleH = current_user.get_hitman_profile()

            if roleH:
                HitFormU.fields['id_hitman'].disabled = True
                HitFormU.fields['description'].disabled = True
                HitFormU.fields['target'].disabled = True

        if HitFormU.is_valid():
            HitFormU.save()
            return redirect('home')
    else:
        HitFormU = HitForm(instance=hitUpdate)

        if current_user.is_hitman and not current_user.is_boss and not current_user.is_manager:
            roleH = current_user.get_hitman_profile()
            if roleH:
                HitFormU.fields['id_hitman'].disabled = True
                HitFormU.fields['description'].disabled = True
                HitFormU.fields['target'].disabled = True

    return render(request, 'hits/update.html', {'HitFormU': HitFormU, 'HitC': statusHit})
