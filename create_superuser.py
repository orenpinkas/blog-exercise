import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()

from django.contrib.auth.models import User

# Create a superuser
username = "oren"
email = "oren@cherrypick-consulting.com"
password = "1234"
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
