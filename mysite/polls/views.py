from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. I have the best wife in the world and I love her to the moon and back <3.")
