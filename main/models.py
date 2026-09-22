from django.db import models  # noqa: F401
import uuid
# Model pertama dibuat pada Drill 1.

class Bookmark(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    label = models.CharField(max_length=100)
    url = models.URLField()
    priority = models.PositiveIntegerField(default=0)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_opened_at = models.DateTimeField(null=True,blank=True)

    class Meta:
        ordering=["-priority","-created_at"]

    def __str__(self):
        return self.label