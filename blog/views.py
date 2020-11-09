from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'proj/Mysite1/market_v2_index.html', {})

def service_detail(request):
    return render(request, 'proj/Mysite1/service_detail.html', {})