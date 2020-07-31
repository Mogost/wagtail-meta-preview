from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from wagtail_meta_preview.meta_settings import IMAGE_DEFAULT_SIZE
from wagtail.images import get_image_model
from wagtail_meta_preview.utils import get_focal


@login_required
def get_image_rendition(request, pk):
    img = get_image_model().objects.get(pk=pk)
    focal = get_focal(img)

    data = {
        "src": img.get_rendition(IMAGE_DEFAULT_SIZE).url,
        "focal": focal,
    }

    return JsonResponse(data)
