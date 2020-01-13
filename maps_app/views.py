from django.shortcuts import render

from .forms import Hangouts_Form
from .models import Hangouts_Model

def view_search(request):
    if request.method == 'POST':
        return view_results(request)

    my_form = Hangouts_Form()
    context = {
        'form' : my_form, 
    }
        
    return render(request, 'maps_app/home.html', context)

def view_results(request):
    if request.method == 'POST':
        # form validation
        my_form = Hangouts_Form(request.POST or None)
        if my_form.is_valid():
            my_form.save()  

        # call the instance of the most recently created object, which contains all the methods and the attributes which were created when the form took in the POST request.
        addrs = Hangouts_Model.objects.latest('id')
        # print (addrs.text)

        if addrs.initialize() == 0:
            return render (request, 'maps_app/no_results.html')
        else:
            addrs.initialize()

        # clear out the form after saving the information
        my_form = Hangouts_Form()
        context = {
            'form' : my_form, 
            'user_add' : addrs.user_addrs_no, 
            'category_result' : addrs.category_result,
            'maps_embed_url' : addrs.maps_embed_hangouts(), 
            'maps_static_user_url' : addrs.maps_static_users(),
        }
        return render (request, 'maps_app/results.html', context)
    
    else:
        return render (request, 'maps_app/enter_search.html')

def view_info(request):
    return render (request, 'maps_app/info.html')