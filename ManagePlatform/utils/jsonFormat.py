from django.http import JsonResponse

from .messageCode import Code


def json_representation(errno=Code.OK, errmsg='', data=None, kwargs=None):
    json_dict = {'errno': errno, 'errmsg': errmsg, 'data': data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)