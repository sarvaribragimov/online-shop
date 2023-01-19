from django.contrib.auth.models import BaseUserManager


class AccoutManager(BaseUserManager):

    # simple user
    def create_user(self,first_name, username, phone_number, password=None):
        if not phone_number:
            raise ValueError("telefon raqam bo'lishi shart")
        if not username:
            raise ValueError("Username is required")

        user = self.model(phone_number=phone_number,username=username,first_name=first_name)
        user.is_active=True
        user.set_password(password)
        user.save(using=self._db)
        return user

    # superuser
    def create_superuser(self, first_name, phone_number, username, password=None):
        user = self.create_user(
            first_name==first_name,
            phone_number=phone_number,
            password=password,
            username=username
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user