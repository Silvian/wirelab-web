from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """User account model manager."""

    def create_user(self, email, password, **extra_fields):
        """Creates and saves a User with the given email and password."""
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, **extra_fields):
        """Creates and saves a staff user with the given email and password."""
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """Creates and saves a superuser with the given email and password."""
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
