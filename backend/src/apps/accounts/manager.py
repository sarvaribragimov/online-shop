from django.contrib.auth.models import BaseUserManager


class AccoutManager(BaseUserManager):

    # simple user
    def create_user(self, email, username, firstname, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # superuser
    def create_superuser(self, email, firstname, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
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
