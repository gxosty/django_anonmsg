import uuid
from django.db import models


class AnonMessage(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	passphrase = models.CharField(max_length=64, null=False, blank=False)
	text_message = models.TextField(null=False, blank=False)