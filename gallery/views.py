from django.shortcuts import render
from .models import Image

# Create your views here.
def index(request):
	images = Image.objects.all()
	return render(request,'index.html',{"images":images})

def search_results(request):
	if request.GET['search']:
		search_term = request.GET.get("search")
		images = Image.search_by_title(search_term)
		message = f"{search_term}"

		return render(request,'search.html',{"message":message,"images":images})
	else:
		message = "You haven't searched for any item"
		return render(request,'search.html',{"message":message})