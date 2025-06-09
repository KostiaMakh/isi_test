from django.contrib.auth import get_user_model
from django.db import models

from apps.core.models import BaseModel


User = get_user_model()


class Thread(BaseModel):
    participants = models.ManyToManyField(User, related_name='threads')

    def __str__(self):
        return f"Thread {self.id}"


class Message(BaseModel):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message {self.id} from {self.sender}"
