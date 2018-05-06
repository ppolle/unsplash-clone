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
		imageLocations = Location.objects.all()
		message = f"{search_term}"

		return render(request,'search.html',{"message":message,"images":images,"imageLocations":imageLocations})
	else:
		message = "You haven't searched for any item"
		imageLocations = Location.objects.all()
		return render(request,'search.html',{"message":message,"imageLocations":imageLocations})

def location(request,location):
	images = Image.filter_by_location(location)
	imageLocations = Location.objects.all()
	return render(request,'location.html',{"images":images,"imageLocations":imageLocations})