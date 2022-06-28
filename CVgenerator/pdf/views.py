from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .form import ProfileForm
from .models import Profile
# for pdf
import pdfkit
from django.template.loader import get_template
import io


def index(request):
    return render(request, 'pdf/resume.html')

def form(request):
    form = ProfileForm()
    name = ''
    phone = ''
    if request.method == 'POST':
# fire des condition pour que ca marche
        form = ProfileForm(request.POST)
        phone = request.POST['phone']
        # if Profile.objects.filter(phone=phone):
        #     messages.error(request, 'this phone exsisted ')
        #     return redirect('delete')
        if form.is_valid():
            form.save()    
            print('valid')
            return redirect(f'/verification/{phone}/')  
    return render(request, 'pdf/form.html',  { 'form': form, 'name':name, 'phone': phone})



def verification(request, phone):
    my_profile = Profile.objects.filter(phone__exact=f"{phone}")
    # pk = my_profile
    # print(dir(my_profile))
    id = my_profile[0].id
    print(id)
    profile = get_object_or_404(Profile, id=id)
    # if request.method == 'POST':
    return render(request, 'pdf/verification.html', { 'profile':profile , 'id':id})

def generate(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    
    template = get_template('pdf/generate.html')
    context = { 'profile':profile }
    html = template.render(context)
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition']='attachement'
    
    return response
    
    
    
    
def download(request):
    pass
    
    









