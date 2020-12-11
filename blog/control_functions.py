def can_new_post(request):
    a = []
    for i in request.user.profile.user_rank.all():
        a.append(i.rank)
    if 'PostCreator' in a:
        return 1
    if 'СуперПользователь' in a:
        return 1
    else:
        return 0


def edit_post(request):
    a = []
    for i in request.user.profile.user_rank.all():
        a.append(i.rank)
    if 'Редактор' in a:
        return 1
    if 'СуперПользователь' in a:
        return 1
    else:
        return 1
