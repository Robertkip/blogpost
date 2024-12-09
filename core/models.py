from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Post(TimeStampedModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ManyToManyField(Category, related_name="posts")

    def __str__(self):
        return self.title
    
class Comment(TimeStampedModel):
    author = models.CharField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on {self.post}"