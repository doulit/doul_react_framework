from django.db import connections
from django.core import serializers
from collections import OrderedDict
from django.http import HttpResponse,JsonResponse
import json

def execute(qs_list):
    print(qs_list)
    return HttpResponse(qs_list, content_type="text/json-comment-filtered")

def execute_and_serialize(qs):
    qs_list = serializers.serialize('json', qs)
    print(qs_list)
    return HttpResponse(qs_list, content_type="text/json-comment-filtered")    
