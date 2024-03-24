from materials.models import Subscription
from config.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from celery import shared_task
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@shared_task
def send_mail_about_update(course_id):
    """Send mail about updating course or lesson to material's owner
    We have to send mail after any change of course or lessons
    So we have to send mail too after creating new lesson, because this is change of course"""
    subs = Subscription.objects.filter(course_id=course_id)
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=EMAIL_HOST_USER, password=EMAIL_HOST_PASSWORD)
    for sub in subs:
        message = MIMEMultipart()
        message['Subject'] = "Updating service"
        message.attach(MIMEText(f"We have to say you about updating materials of course: '{sub.course.title}'",
                                'plain'))
        connection.sendmail(from_addr=EMAIL_HOST_USER, to_addrs=sub.user.email, msg=message.as_string())
    connection.close()
