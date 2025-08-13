from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_email_view(email):
    subject = 'you have been assigned to a Defect task complete ASAP!!'
    message = 'the given High priority defect need to complete'
    from_email = 'dgunadhana@gmail.com'
    recipient_list = [email]
    html_message = render_to_string('defects/task_email_template.html')
    plain_message = strip_tags(html_message)
    
    try:
        send_mail(subject=subject,
                  message=message,
                  from_email=from_email,
                  recipient_list=recipient_list,
                  html_message=html_message,
                  fail_silently=False,
                  )
        return HttpResponse('Email sent successfully')
    except Exception as e:
        return HttpResponse(f"error sending Email: {str(e)}")
        