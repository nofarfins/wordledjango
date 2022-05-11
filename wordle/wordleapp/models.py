from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator as MinValue, MaxValueValidator as MaxValue
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Game(BaseModel):

    LEVELS =(
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    )

    level = models.CharField(max_length=16, choices=LEVELS)
    player = models.ForeignKey(User, on_delete=models.PROTECT)
    success = models.BooleanField(default=False)

    class Meta:
        db_table = 'games'


class Categories(BaseModel):
    CATEGORIES = (
        ('Movies', 'Movies'),
        ('NBA players', 'NBA players'),
        ('Fruit', 'Fruit'),
        ('Countries', 'Countries'),

    )
    name = models.CharField(max_length=16, choices=CATEGORIES)


class Profile(BaseModel):
    player = models.OneToOneField(User, on_delete=models.PROTECT)
    games = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)


