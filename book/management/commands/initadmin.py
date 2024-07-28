from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Will create a superuser if the base is empty.
    Command to start: python3 manage.py initadmin
    """

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = "root"
            email = "111@gmail.com"
            password = "12345678"
            print("Creating account")
            admin = User.objects.create_superuser(
                email=email, password=password, username=username
            )
            admin.is_active = True
            admin.is_admin = True
            admin.is_staff = True
            admin.save()

        else:
            print("Admin accounts can only be initialized if no Accounts exist")
