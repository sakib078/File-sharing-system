
from users.models import User

from django.shortcuts import render, get_object_or_404


users = User.objects.all()

for user in users:
    print(user)
