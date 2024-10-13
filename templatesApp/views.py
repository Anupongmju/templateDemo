from django.shortcuts import render


def renderTemplate(request):
    myDict={"name":"Anupong Mabunrueang"}
    return render(request, 'templatesApp/firstTemplate.html',context=myDict)


def renderEmployee(request):
    myDict={"id":6604101396,"name":"Anupong Mabunrueang","sal":10000}
    return render(request, 'templatesApp/employeeTemplate.html',context=myDict)