# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from util.normal import ensure_unicode

push_key = u"mt1994"


@csrf_exempt
def gallery(request):
    result = {
        "status": "failed"
    }
    if request.method == 'POST':
        received_json_data = json.loads(ensure_unicode(request.body))
        key = received_json_data.get("key", "")
        print key
        if key != push_key:
            result['msg'] = "not authorize"
        else:
            result['status'] = "success"
            print received_json_data
    else:
        result['msg'] = "need post"
    return HttpResponse(json.dumps(result), content_type='application/json')
