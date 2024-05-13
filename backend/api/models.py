from django.db import models
from register.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

TYPE_SET = (
    ("web", "WEB"),
    ("line", "LINE"),
)

TIME_SET = (
    ("1", "〜15分"),
    ("2", "15分〜45分"),
    ("3", "45分〜90分"),
    ("4", "90分~180分"),
    ("5", "180分〜")
)
    
LEVEL_SET = (
    ("1", "初級"),
    ("2", "初中級"),
    ("3", "中級"),
    ("4", "上級"),
    ("5", "超上級")
)

class CreatorModel(models.Model):
    name = models.CharField(max_length=120)
    image = models.FileField()
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RiddleModel(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    type = models.CharField(choices=TYPE_SET, max_length=10)
    time = models.CharField(choices=TIME_SET, max_length=10)
    level = models.CharField(choices=LEVEL_SET, max_length=10)
    rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rating_sukkiri = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rating_story = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    rating_gimmick = models.FloatField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(CreatorModel, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    bookmarks = models.ManyToManyField(User, verbose_name="ブックマークユーザー", blank=True)
    playings = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name