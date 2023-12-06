from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def Manager(request):
    tenn = tenant.objects.all()
    return render(request, "Man_home.html",{"tenants":tenn} )

def  AddTenants(request):

    if request.method == "POST":
        form = AddTenant(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Manager')
    else:
        form = AddTenant()
    return render(request, "Man_addTen.html", {'form':form})

def UpdateTen(request, ID):
    item = tenant.objects.get(ID=ID)
    form = UpdateTenant(instance=item)
    if request.method == 'POST':
        form = UpdateTenant(request.POST, instance=item)
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('Manager')
    else:
        form = UpdateTenant(instance=item)

    return render(request,
                  'Man_UpdateTen.html',
                  {'form': form})

def DeleteTen(request, ID):
    item = tenant.objects.get(ID=ID)
    form = AddTenant(instance=item)
    if request.method == 'POST':
            item.delete()
            return redirect('Manager')
    else:
        form = UpdateTenant(instance=item)

    return render(request,
                  'Man_DeleteTen.html',
                  {'item': item})

def Tenant(request,apartments):
    tenn = requests.objects.filter(apartment__contains = apartments)
    return render(request, "Ten_home.html", {"tenants": tenn})

def  Addrequests(request,apartments):

    if request.method == "POST":
        form = AddRequest(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.apartment = apartments
            obj.status = "pending"
            obj.save()
            return redirect('/Tenant/'+apartments+'/')
    else:
        form = AddRequest()
    return render(request, "Ten_CreateRequest.html", {'form':form})

def Staff(request):
    search_items = request.GET.get('search')

    if search_items:
        items = requests.objects.filter(Q(ID__icontains=search_items) |
                                         Q(apartment__icontains=search_items) |
                                         Q(desc__icontains=search_items)|
                                         Q(status__icontains=search_items)|
                                         Q(area__icontains=search_items))
    else:
        # If not searched, return default posts
        items = requests.objects.all()


    return render(request, "Staff_home.html", {"storeItem":items})

def request(request,ID):
    item = requests.objects.get(ID=ID)
    if request.method == 'POST':
            item.status = "complete"
            item.save()
            return redirect('/Staff/')

    return render(request,
                  'Staff_Request.html',
                  {'item': item})

