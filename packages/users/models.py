from logging import getLogger

from tortoise import fields
from tortoise.exceptions import DoesNotExist, IntegrityError
from tortoise.models import Model
from typing import Tuple, Type, TypeVar

USER = TypeVar("USER", bound="User")
logger = getLogger('log_print')

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    role = fields.CharField(max_length=50)
    name = fields.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username
    
    @classmethod
    async def update_or_create(cls, username: str, **kwargs) -> Tuple[USER, bool]:
        logger.debug(f"Update or create User {username}")
        try:
            user = await cls.get(username=username)
        except DoesNotExist:
            try:
                user = await cls.create(username=username, **kwargs)
                return user, True
            except IntegrityError as err:
                logger.error(f"{err} - Cant Create User ({username})")
                return None, False

        await user.update_from_dict(kwargs).save()
        return user, False

    @classmethod
    async def get_or_create(cls, username: str, **kwargs) -> Tuple[Type[USER], bool]:
        """Get or create user by username

        Args:
            username (str): username of user
            **kwargs: additional fields

        Returns:
            (User, bool): user and created flag
        """
        logger.debug(f"Get or create User {username}")
        try:
            user = await cls.get(username=username)
            return user, False
        except DoesNotExist:
            try:
                user = await cls.create(username=username, **kwargs)
                logger.debug(f"User({user}) created")
                return user, True
            except IntegrityError as err:
                logger.error(f"{err} - Cant Create User ({username})")
                return None, False

    class Meta:
        table = "user_profile"
