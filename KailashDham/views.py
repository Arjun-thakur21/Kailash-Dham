from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from Home import models
from Home.models import Contact,Service,Rating,Properties,Agents,About,Team
from django.core.paginator import Paginator

# from Home.models import Image

def homepage(request):
    
    servicesData = Service.objects.all()
    ratingsData = Rating.objects.all()
    propertiesData=Properties.objects.all()
    agentsData=Agents.objects.all()
    aboutData=About.objects.all()
    # imageData=Image.objects.all()

    data = {
        'servicesData': servicesData,
        'ratingsData': ratingsData,
        'propertiesData':propertiesData,
        'agentsData':agentsData,
        'aboutData':aboutData,
        # 'imageData':imageData
    }
    return render(request, "index.html", data)
def contact(request):
    if request.method == "POST":
        if request.POST.get('name') == "":    
          return render(request,"contact.html",{'error':True})
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
       
        Cn=Contact(name = name, email= email, subject= subject, message = message )
        Cn.save()
    
    return render(request,"contact.html")

def properties(request):
    propertiesData = Properties.objects.select_related('agent').all()
    paginator = Paginator(propertiesData, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data={
        'propertiesData':propertiesData,
        'page_obj': page_obj
        
    }
    return render(request,"properties.html", data)

def propertysingle(request, id):
    propertyData = get_object_or_404(Properties, id=id)
    agentsData = propertyData.agent 

    data = {
        'propertyData': propertyData,
        'agentsData': agentsData
    }
    return render(request, "property-single.html", data)


def aboutus(request):
    aboutData=About.objects.all()
    teamData=Team.objects.all()

    data={
        'aboutData':aboutData,
        'teamData':teamData
    }
    return render(request,"about.html",data)

def services(request):
    servicesData = Service.objects.all()

    data ={
        'servicesData': servicesData
    }
    return render(request,"services.html",data)

def service_details(request, id):
    service = get_object_or_404(Service, id=id)
    other_services = Service.objects.exclude(id=id)  

    context = {
        'serviceData': service,
        'otherServices': other_services,
    }
    return render(request, 'service-details.html', context)

def search_properties(request):
    query = request.GET.get('q')  
    if query:
        results = Properties.objects.filter(
            Properties_address__icontains=query
        )  # You can also search other fields like 'Properties_name' or 'Properties_desc'
    else:
        results = None

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'search_results.html', context)