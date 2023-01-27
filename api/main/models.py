from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title + " (" + str(self.id) + ")"







class Wallet(models.Model):
    username = models.CharField(max_length=120)
    public_key = models.CharField(max_length=120)
    private_key = models.CharField(max_length=120)

    status = models.BooleanField(default=False)

    def __str__(self):
        return self.username
