from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here
def members(request):
    mymembers = Member.objects.all().all()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymembers': mymember,
    }
    return HttpResponse(template.render(context, request))