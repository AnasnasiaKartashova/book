import smtplib
from celery import shared_task
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER, EMAIL_RECIPIENT


@shared_task
def send_message_for_user() -> bool | dict[str, str]:
    """
    A Celery task to send an email message to a user indicating the server's status
    """
    email_recipient = EMAIL_RECIPIENT
    subject = "Информация о работе сервера"
    message = "Сервер работает стабильно"
    try:
        send_mail(subject, message, EMAIL_HOST_USER, [email_recipient])
        return True
    except smtplib.SMTPDataError:
        return {"Error": "Email failed. You sent too many messages"}
    except smtplib.SMTPAuthenticationError:
        return {
            "Error": "Email failed. You have entered an incorrect login or password"
        }
    except (smtplib.SMTPRecipientsRefused, smtplib.SMTPSenderRefused):
        return {"Error": "Email failed. Message sending error"}
    except ValueError:
        return {"Error": "Email failed.  Invalid recipient address"}
