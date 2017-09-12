from celery.decorators import task
from celery.utils.log import get_task_logger

from .emails import send_notification_email

logger = get_task_logger(__name__)

@task(name="send_notification_email_task")
def send_notification_email_task(subject, message):
    logger.info("Send notification email")
    return send_notification_email(subject, message)
