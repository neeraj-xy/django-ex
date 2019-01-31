from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            feedback = myForm.cleaned_data['feedback']

            context = {
            'name': name,
            'email': email,
            'feedback': feedback
            }

            template = loader.get_template('thankyou.html')

            #returing the template
            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()
     #returning form

     return render(request, 'responseform.html', {'form':form});
