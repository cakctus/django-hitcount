from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
from hitcount.models import HitCount


from hit.models import HitCount as HitModel

from django.views.generic.detail import DetailView


from django.http import JsonResponse


def get_hit_count(request, endpoint):
    hit_count = get_object_or_404(HitCount, id=endpoint)
    return JsonResponse({'hit_count': hit_count.hits})


class CustomHitCountDetailView(HitCountDetailView):
    model = HitModel
    count_hit = True

    def get_object(self):
        endpoint_path = self.kwargs.get('endpoint_path')
        hit_count, created = HitModel.objects.get_or_create(
            endpoint=endpoint_path)
        return hit_count

    def render_to_response(self, context, **response_kwargs):

        print("Hit Count Object:", self.object.endpoint)

        hit_count = self.object.hits if hasattr(self, 'object') else 0
        hits = HitCount.objects.get(id=self.object.id)
        response_data = {
            'endpoint': self.object.endpoint if hasattr(self, 'object') else None,
            'hit_count': hit_count,
            'id': self.object.id,
            # 'hits': get_object_or_404(HitCount, id=self.object.id).hits
            'hits_id': hits.id,
            'hits': hits.hits
        }

        return JsonResponse(response_data)
