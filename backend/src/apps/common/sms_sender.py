import random
import string
from datetime import date, timedelta

import requests

from .models import SMSLog, SMSToken

today = date.today()


class BaseAPI:
    """
    Base API - for Eskiz token
    method: get_token, set_token, create_token, _call, refresh_token
    """

    base_url = "https://notify.eskiz.uz/api"
    email = "sarvaribragimov174@gmail.com"
    password = "Q7wwuVwG3wWo5KlhJH7xkgvU63b5azFo4kZTSrn4"

    def get_token(self):
        """
        Get token from database if token is expired then refresh token and return new token
        """
        sms_token_obj = SMSToken.objects.all()
        if sms_token_obj.exists():
            token = sms_token_obj.first()
            return self.set_token() if token.expires_at <= today else token.token
        return self.set_token()

    def set_token(self):  # sourcery skip: raise-specific-error
        """
        Create token and save to database
        """
        try:
            resp = requests.post(f"{self.base_url}/auth/login", data={"email": self.email, "password": self.password})
            data = resp.json()
            if resp.status_code != 200:
                raise Exception(data["message"])
            token = data["data"]["token"]
            self.create_token(token)  # call create token  to database
            return token
        except Exception as e:
            raise Exception(e) from e

    def create_token(self, token):
        """
        Create token and save to database with expires date
        """
        SMSToken.objects.create(name="SMS Token", token=token, expires_at=today + timedelta(days=29))

    def _call(self, endpoint, body=None):  # sourcery skip: raise-specific-error
        """
        Call API with token
        """
        try:
            token = self.get_token()
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

            resp = requests.post(endpoint, json=body, headers=headers)
            return resp.status_code == 200
        except Exception as e:
            raise Exception(e) from e


class SendSMS(BaseAPI):
    """
    Send SMS with token
    use: SendSMS.send_sms(phone, message)
    """

    sms_nickname = 4546  # sms nickname

    def send_sms(self, phone, message):
        """
        Send sms with token
        """
        try:
            endpoint = f"{self.base_url}/message/sms/send"
            body = {
                "mobile_phone": phone,
                "message": str(message),
                "from": self.sms_nickname,
            }
            self._call(endpoint, body=body)
            self.create_sms_log(phone, message)

            return {"status": True, "message": "SMS sent successfully"}
        except Exception as e:
            return {"status": False, "message": str(e)}

    def create_sms_log(self, phone, message):
        """
        Create sms log in database
        """
        SMSLog.objects.create(phone=phone, message=message, status=True)

    def generate_one_time_sms(self, length=6):
        """
        Generate one time sms code
        """
        return "".join(random.choice(string.digits) for _ in range(length))
