from django.shortcuts import render
from .models import Image,Location,Category

# Create your views here.
def index(request):
	images = Image.objects.all()
	imageLocations = Location.objects.all()
	return render(request,'index.html',{"images":images,"imageLocations":imageLocations})

def search_results(request):
	if request.GET['search']:
		search_term = request.GET.get("search")
		images = Image.search_by_title(search_term)
		message = f"{search_term}"

		return render(request,'search.html',{"message":message,"images":images})
	else:
		message = "You haven't searched for any item"
		return render(request,'search.html',{"message":message})

def location(request,location):
	images = Image.objects.filter(image_location__location__startswith = location)
	return render(request,'location.html',{"images":images})