from django.shortcuts import render
from django import forms
from .models import solventForm
# Create your views here.
def index(request):
    return render (request, "solvent/home.html" )

def aboutus(request):
 	return render(request, "solvent/aboutus.html")

def buy(request):
 	return render(request, "solvent/buy.html")

def contactus(request):
 	return render(request, "solvent/contactus.html")

def forrent(request):
 	return render(request, "solvent/forrent.html")

def land(request):
 	return render(request, "solvent/land.html")


class solventProForm(forms.ModelForm):
    name = forms.CharField( label='', widget=forms.TextInput(attrs={"placeholder": "Name"}))
    email = forms.EmailField( label='', widget=forms.EmailInput(attrs={"placeholder": "Email"}))
    phone = forms.IntegerField( label='', widget=forms.NumberInput(attrs={"placeholder": "Phone"}))
    describe = forms.CharField( label='', widget=forms.TextInput(attrs={"placeholder": "Describe Your Search"}))
    class Meta:
        model = solventForm
        fields = ['name', 'email', 'phone', 'state', 'location', 'houses', 'describe']
        # exclude = ['id']
    def __init__(self, *args, **kwargs):
        super(solventProForm, self). __init__(*args, **kwargs)
        self.fields['state'].label=''
        self.fields['location'].label=''
        self.fields['houses'].label=''

def solventProperty(request):
    
    form = solventProForm()
    if request.method == "POST":
        form = solventProForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            solventPropertyForm = form.save(commit=False)
            print(solventPropertyForm)
            solventPropertyForm.save()
            msg = "submitted successfully we'll get back to you"
            return render(request, "solvent/solventform.html", {"solventPropertyForm" :form, "msg" : msg})
    return render(request, "solvent/solventform.html", {"solventPropertyForm" :form}) 	

def buy(request):
    
    form = solventProForm()
    if request.method == "POST":
        form = solventProForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            solventPropertyForm = form.save(commit=False)
            print(solventPropertyForm)
            solventPropertyForm.save()
            msg = "submitted successfully we'll get back to you"
            return render(request, "solvent/buy.html", {"solventPropertyForm" :form, "msg" : msg})
    return render(request, "solvent/buy.html", {"solventPropertyForm" :form}) 

def forrent(request):
    
    form = solventProForm()
    if request.method == "POST":
        form = solventProForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            solventPropertyForm = form.save(commit=False)
            print(solventPropertyForm)
            solventPropertyForm.save()
            msg = "submitted successfully we'll get back to you"
            return render(request, "solvent/forrent.html", {"solventPropertyForm" :form, "msg" : msg})
    return render(request, "solvent/forrent.html", {"solventPropertyForm" :form})

def land(request):
    
    form = solventProForm()
    if request.method == "POST":
        form = solventProForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            solventPropertyForm = form.save(commit=False)
            print(solventPropertyForm)
            solventPropertyForm.save()
            msg = "submitted successfully we'll get back to you"
            return render(request, "solvent/land.html", {"solventPropertyForm" :form, "msg" : msg})
    return render(request, "solvent/land.html", {"solventPropertyForm" :form})

def index(request):
    
    form = solventProForm()
    if request.method == "POST":
        form = solventProForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            solventPropertyForm = form.save(commit=False)
            print(solventPropertyForm)
            solventPropertyForm.save()
            msg = "submitted successfully we'll get back to you"
            return render(request, "solvent/home.html", {"solventPropertyForm" :form, "msg" : msg})
    return render(request, "solvent/home.html", {"solventPropertyForm" :form})






    
