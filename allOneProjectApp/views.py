from django.shortcuts import render
from allOneProjectApp.models import onePiece
from allOneProjectApp.forms import onePieceForms
# Create your views here.

def form_display(request):
	if request.method=='GET':
		form=onePieceForms()
		my_display={'form':form}
		return render(request,'allOneProjectApp/display.html',context=my_display)

	if request.method=='POST':
		form=onePieceForms(request.POST)

		if form.is_valid():
			form.save()

	form=onePieceForms()
	return render(request,'allOneProjectApp/display.html',context={'form':form})