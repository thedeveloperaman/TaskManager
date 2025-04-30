from django.db import models

class Task(models.Model):
    """
    Model representing a task with a title, completion status, and category.
    """
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('shopping', 'Shopping'),
        ('study', 'Study'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')

    def __str__(self):
        return self.title
