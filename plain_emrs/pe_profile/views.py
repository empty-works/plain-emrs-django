from django.shortcuts import render
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse
#from django.template import loader


@login_required
def pe_profile(request):
    #template = loader.get_template('index.html') 
    #return HttpResponse(template.render())
    context = {
    }
    return render(request, 'index.html', context=context)
