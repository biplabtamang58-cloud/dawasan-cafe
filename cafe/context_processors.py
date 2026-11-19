from .models import CafeInfo


def cafe_info(request):
    return {'info': CafeInfo.objects.first()}