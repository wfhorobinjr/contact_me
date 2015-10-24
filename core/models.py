from django.db import models

TITLE_CHOICES = (
(0, "Mr."),
(1, "Ms."),
(2, "Mrs."),
(3, "Dr."),
)

class Contact(models.Model):
  name = models.CharField(max_length=300, default='Name')
  email = models.EmailField(max_length=250)
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  title = models.IntegerField(choices=TITLE_CHOICES, default=0)

  def __unicode__(self):
    return self.name
# Create your models here.
