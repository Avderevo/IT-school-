from app import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse


def send_mail(to, template, context):
    html_content = render_to_string(
        'emails/{}.html'.format(template), context)
    text_content = render_to_string(
        'emails/{}.txt'.format(template), context)

    msg = EmailMultiAlternatives(
        context['subject'], text_content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_confirm_email(request, email, code):
    context = {
        'subject': ('Profile activation'),
        'uri': request.build_absolute_uri(
            reverse('confirm', kwargs={'code': code})),
    }
    send_mail(email, 'activate_profile', context)


def send_reset_password_email(request, email, token, uid):
    context = {
        'subject': ('Restore password'),
        'uri': request.build_absolute_uri(
            reverse('restore_password', kwargs={
                'uidb64': uid, 'token': token})),
    }

    send_mail(email, 'restore_password_email', context)
