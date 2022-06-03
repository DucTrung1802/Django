from email.policy import default
from django.db import models
import uuid

# Create your models here.

# "null" is set to True if: we are allowed to create a record or a row in the database of this value and we don't need to set a description. (for Database)

# "blank" is set to True means that whenever we're submitting some kind of form or making a post request, we can submit this value with this field being blank. (for Django)


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return self.title
