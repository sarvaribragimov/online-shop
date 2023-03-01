from django.contrib.auth.models import BaseUserManager


class AccoutManager(BaseUserManager):

    # simple user
    def create_user(self, phone_number, username, firstname, password=None):
        if not phone_number:
            raise ValueError("phone_number is required")
        if not username:
            raise ValueError("Username is required")

        user = self.model(
            phone_number=phone_number,
            username=username,
            firstname=firstname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # superuser
    def create_superuser(self, phone_number, firstname, username, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            username=username,
            firstname=firstname,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
