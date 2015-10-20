from nat.models import User


def register_user(username, user_password):
    user = User(user_name=username, password=user_password)
    user.save()
    return user.id

def log_in(username, user_password):
    users = User.objects.all()

    for user in users:
        if user.user_name == username and user.password == user_password:
            global loggedInUser
            loggedInUser =user
            return user

    return None

def get_loggedInUser():
    return loggedInUser


def printMes():
    print 'OOOOOOO'

