from django.urls import resolve
from .models import HitCount


class HitCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware called for:", request.path)
        response = self.get_response(request)

        if request.path.startswith('/api/hitcount/'):
            endpoint = resolve(request.path_info).kwargs.get('endpoint')
            print("Endpoint:", endpoint)
            if endpoint:
                try:
                    instance = HitCount.objects.get(id=endpoint)
                except HitCount.DoesNotExist:
                    new = HitCount(id=endpoint)
                    new.save()
        return response
