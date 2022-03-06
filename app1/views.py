from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request,'main.html')


def removed(request):
    dj = request.POST.get('text','default')
    room = request.POST.get('room', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'off')
    space = request.POST.get('space', 'off')
    Count = request.POST.get('Count', 'off')


    if room == "on":
        punctuations= '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in dj:
            if char not in  punctuations:
                analyzed = analyzed + char

        context ={'purpose':'-' , 'removal_text': analyzed}
        return render(request, 'submit.html',context )

    elif (fullcaps == "on"):
        analyzed= ""
        for char in dj:
            analyzed = analyzed + char.upper()

        context ={'purpose':'-' , 'upper_case': analyzed}
        return render(request, 'room.html',context )

    elif (newline == "on"):
        analyzed= ""
        for char in dj:
            if char!="/n" and char!="/r":
                analyzed = analyzed + char

        context ={'purpose':'-' , 'new_line': analyzed}
        return render(request, 'newline.html',context )

    elif (space == "on"):
        analyzed= ""
        for index, char in enumerate(dj):
            if not(dj[index]==" " and dj[index+1]==" "):
                analyzed = analyzed + char

        context ={'purpose':'-' , 'removal_space': analyzed}
        return render(request, 'space.html',context )

    elif (Count == "on"):
        l = len(dj) - dj.count(' ')
        context ={'purpose':'-' , 'Count': l}
        return render(request,'count.html',context )

    else:
        return HttpResponse('error')       
        


