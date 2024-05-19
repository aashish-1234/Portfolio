from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

from contactdetail.models import contactDetail
from django.core.mail import send_mail


def __str__(self):
    pass

class Meta:
    db_table = ''
    managed = True
    verbose_name = 'ModelName'
    verbose_name_plural = 'ModelNames'

def homePage(request):
    
    # data={
    #     'title':'home page',
    #     'bdata':'welcome to django project',
    #     'clist': ['php','java','django'],
    #     'student_details':[
    #         {'name':'aashish','phone':945464602},
    #         {'name':'mohan','phone':7784456564},
    #     ]
    # }
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("welcome to codestudyindian")

def project(request):
    return render(request,"project.html")

# def course(request, courseid):
#     return HttpResponse(courseid)

def contact(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"contact.html",{'output':output})

def about_me(request):
    # finalans=0
    # data={}
    # try:
    #     if request.method== "POST":

    #         # n1=int(request.GET['num1'])
    #         # n2=int(request.GET['num2'])
    #         n1=int(request.POST.get('num1'))
    #         n2=int(request.POST.get('num2'))
    #         finalans=n1+n2
    #         data={
    #             'n1':n1,
    #             'n2':n2,
    #             'output':finalans
    #         }
    #         url="/contact/?output={}".format(finalans)
    #         #return HttpResponseRedirect(url)
    #         return redirect(url)
    # except:
    #     pass
    return render(request,"about.html")

def skill(request):
    return render(request,"skill.html")

# def submitForm(request):
    # finalans=0
    # data={}
    # try:
    #     if request.method== "POST":

    #         # n1=int(request.GET['num1'])
    #         # n2=int(request.GET['num2'])
    #         n1=int(request.POST.get('num1'))
    #         n2=int(request.POST.get('num2'))
    #         finalans=n1+n2
    #         data={
    #             'n1':n1,
    #             'n2':n2,
    #             'output':finalans
    #         }
    #         return HttpResponse(finalans)
    # except:
    pass

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        en=contactDetail(name=name,email=email,message=message,subject=subject)
        en.save()

        send_mail(
            "Receiving your email",
            "thank you for contacting me i will be response soon",
            'hiaashish83@gmail.com',
            [email],
            fail_silently=False,
        )
        data={
            'output':"success_mail"
        }
    return render(request,"contact.html",data)

