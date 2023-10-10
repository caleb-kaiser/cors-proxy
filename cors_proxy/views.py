from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def cors_proxy(request):
    external_site_url = "https://www.comet.com/api/auth/new"
    
    if request.method == "POST":
        headers = {
            'Content-Type': 'application/json',
        }

        response = requests.post(external_site_url, headers=headers, data=request.body)

        # You can add any additional logic here, e.g., handling different HTTP response codes.

        return JsonResponse(response.json(), status=response.status_code)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)
