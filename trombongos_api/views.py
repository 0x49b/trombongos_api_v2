from django.shortcuts import redirect


def root_view(request):
    # Your view logic here

    # Redirect to another URL path
    return redirect('/api/v1/')
