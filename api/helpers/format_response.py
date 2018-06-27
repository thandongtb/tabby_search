from django.http import JsonResponse

def format(code = 200, data = None, message = 'Default response message', errors = None):
    return JsonResponse(
        {
            'code': code,
            'data': data,
            'message': message,
            'errors': errors
        }
    )