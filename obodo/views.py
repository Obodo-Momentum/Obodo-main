from django.shortcuts import render

# Create your views here.
def home(request):
    data={"team_name": "Team Obodo", "greeting": "Hello" }
    return render(request, 'frontend/index.html', {"data_from_view_context": data})
