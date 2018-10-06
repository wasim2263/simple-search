from django.shortcuts import render
from django.http import HttpResponse
from .models import Developers, Languages, ProgrammingLanguages


# Create your views here.


def index(request):
    try:
        language_search = request.GET['srchlang'];
        if (language_search == ''):
            raise Exception('no filter added')

        language_search = formatRequst(language_search);
        languages = Languages.objects.filter(code__in=language_search)
    except:
        languages = Languages.objects.all()
    try:
        programming_anguage_search = request.GET['srchproglang'];
        if (programming_anguage_search == ''):
            raise Exception('no filter added')

        programming_anguage_search = formatRequst(programming_anguage_search);
        programming_languages = ProgrammingLanguages.objects.filter(name__in=programming_anguage_search)

    except:
        programming_languages = ProgrammingLanguages.objects.all()

    developer_list = Developers.objects.filter(languages__in=languages,
                                               programming_languages__in=programming_languages).distinct()

    context = {'developer_list': developer_list}
    # return  HttpResponse(developer_list)
    return render(request, 'developersearch/index.html', context)


# def filterDev(request):
#     developer_list = Developers.objects.filter(languages=['3','2'])
#     context = {'developer_list': developer_list}
#     return  HttpResponse(developer_list,)
# return render(request, 'developersearch/index.html', context)

def formatRequst(value):
    value = value.replace(',', ' ')
    return value.split(' ')

def filterLnaguage(request):
    language_list = Languages.objects.filter(developers=None)
    print(language_list)
    context = {'language_list': language_list}
    return render(request, 'developersearch/language.html', context)

