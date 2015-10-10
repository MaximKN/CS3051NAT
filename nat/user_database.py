import django
from nat.models import User


def register_user(username, user_password):
    user = User(user_name=username, password=user_password)
    user.save()
    return user.id


def get_user(userId):
    return User.objects.get(id=userId)

