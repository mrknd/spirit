from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

from .models import Contact


# For Contact Form
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        # customer_need = request.POST['customer_need']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already contacted this car.')
                return redirect('/cars/' + car_id)

        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id,
                          first_name=first_name,
                          phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Car Inquiry",
            f"You have a new inquiry for the car {car_title}.",
            "vatikan98@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your message has been sent.')
        return redirect('/cars/' + car_id)


def inquiry_short(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(
            first_name=first_name,
            phone=phone,
            message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            "New Car Inquiry",
            f"You have a new inquiry for the car",
            "vatikan98@gmail.com",
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, 'Your message has been sent.')
        return redirect('home')
