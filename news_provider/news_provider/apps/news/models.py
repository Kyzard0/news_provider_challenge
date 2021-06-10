import uuid

from django.db import models


class Author(models.Model):
    """
    Author model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, auto_created=True)
    name = models.CharField(max_length=50)
    picture = models.ImageField(null=True, default=None,)

    def __str__(self):
        return self.name


class Article(models.Model):
    """
    Article model
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False, auto_created=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='articles')
    category = models.CharField(max_length=15)
    title = models.CharField(max_length=150)
    summary = models.TextField()
    firstParagraph = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title
