from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(
        request,
        'main/base_full_width.html',
    )
@login_required
def index(request):
    return render(
        request,
        'main/base_full_width.html',
    )

