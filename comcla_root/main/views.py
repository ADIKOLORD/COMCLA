from django.shortcuts import render, redirect

from main.models import Contact


def main_page(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        phone = request.POST['Phone Number']
        text = request.POST['Message']
        if name != '' and email != '' and text != '':
            Contact.objects.create(name=name, email=email, phone=phone, message=text)
        return redirect('home')

    return render(request, 'index.html')
