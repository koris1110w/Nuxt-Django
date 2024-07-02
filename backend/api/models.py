from django.db import models
from register.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from markdownx.models import MarkdownxField

TYPE_SET = (
    ("web", "WEB"),
    ("line", "LINE@"),
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
    description = models.TextField(null=True, blank=True)
    content = MarkdownxField(null=True, blank=True) 
    url = models.CharField(max_length=255)
    type = models.CharField(choices=TYPE_SET, max_length=10)
    rating = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    level = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    time = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sukkiri = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    story = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    gimmick = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(CreatorModel, on_delete=models.CASCADE)
    bookmarks = models.ManyToManyField(User, verbose_name="ブックマークユーザー", blank=True)
    playings = models.IntegerField(null=True, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    review = MarkdownxField(null=True, blank=True) 

    def __str__(self):
        return self.name
    
class ReviewModel(models.Model):
    user = models.ForeignKey(User, verbose_name="投稿者", on_delete=models.CASCADE)
    riddle = models.ForeignKey(RiddleModel, verbose_name="謎", on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    time = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sukkiri = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    story = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    gimmick = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

class ArticleModel(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='')
    description = models.TextField(null=True, blank=True)
    riddles = models.ManyToManyField(RiddleModel, verbose_name="紹介謎", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title