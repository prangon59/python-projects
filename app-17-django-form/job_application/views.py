from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            # Saveing the form data to the database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)

            # Send email to the user
            message_body = (
                f"Thank you for submitting your application.\n"
                f"Here is a summary of your application:\n"
                f"Name: {first_name} {last_name}\n"
                f"Email: {email}\n"
                f"Occupation: {occupation}\n"
                f"Date: {date}\n"
                f"Thank you!"
                )
            email_message = EmailMessage("Form submitted", message_body, to=[email])
            email_message.send()
            
            messages.success(request, "Form submitted successfully!")
            return redirect('index')

    return render(request, "index.html")