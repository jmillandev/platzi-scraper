from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        table = "user_profile"
