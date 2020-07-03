from django.db import models

class feedback(models.Model):
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=1000, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.name

class order(models.Model):
    name_o = models.CharField(max_length=30, null=True)
    email_o = models.CharField(max_length=50, null=True)
    message_o = models.CharField(max_length=9000, null=True)

    def __str__(self):
        return self.name_o
