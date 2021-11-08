from django.db import models
from accounts.models import CustomUser


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class File(models.Model):
    name        = models.CharField(max_length=100, null=False)
    file_type   = models.CharField(max_length=100, default='draft')
    file        = models.FileField(upload_to=user_directory_path)
    created_by  = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    created_on  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.file.name}'
