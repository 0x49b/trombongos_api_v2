from django.shortcuts import redirect, render


def root_view(request):
    # Your view logic here

    # Redirect to another URL path
    return redirect('/api/v1/')


def saison_view(request):
    return render(request, 'saison.html')
