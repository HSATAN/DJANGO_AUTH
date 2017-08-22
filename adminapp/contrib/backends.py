# conding=utf8

from adminapp.models import UserModel


class UserBackend(object):

    def authenticate(self, request, **info):
        print info
        user = UserModel.objects.get(pk=1)
        if user:
            print user
            return user
    def get_user(self, id):
        try:
            return UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return None

