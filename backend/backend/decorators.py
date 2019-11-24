from functools import wraps
from django.views.decorators.csrf import csrf_exempt


def api_view(view_fn):
    @csrf_exempt
    @wraps(view_fn)
    def wrap(request, *args, **kwargs):
        return view_fn(request, *args, **kwargs)
    return wrap

