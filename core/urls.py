from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_view(request):
    return JsonResponse({
        "movies": [
            {"title": "The Shawshank Redemption", "release_year": 1994},
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
]
