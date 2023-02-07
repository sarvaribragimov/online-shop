from django.core.mail import EmailMessage
from .timer import timer


@timer
async def send_email_async(subject, body, to):
    """Send email async

    Args:
        subject (_type_): Subject of email
        body (_type_): Body of email
        to (list): Email address of recipient

    Returns:
        _type_: True if email sent successfully, False otherwise
    """
    try:
        sendmail = EmailMessage(
            subject=subject,
            body=body,
            to=to,
        )
        await sendmail.send()
    except Exception as e:
        print(e)
        return False
    return True
