from nat.models import User

global loggedInUser
loggedInUser = None

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

def logOut():
    global loggedInUser
    loggedInUser = None

def addFavouriteArticle(favouriteArticle):
    global loggedInUser
    if loggedInUser is not None:
        loggedInUser.favourite_article.add(favouriteArticle)

def getFavouriteArticle():
    global loggedInUser
    if loggedInUser is not None:
        return loggedInUser.favourite_article.all()

def get_loggedInUser():
    global loggedInUser
    return loggedInUser

