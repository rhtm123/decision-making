from django.db import models

class Decision(models.Model):
    text = models.CharField(max_length=255, blank=True, null=True)
    name1 = models.CharField(max_length=255)
    name2 = models.CharField(max_length=255)
    popularity = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    ##tracking
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "{} vs {}".format(self.name1, self.name2)

class Point(models.Model):
    name = models.CharField(max_length=255)
    given_points_1 = models.IntegerField(default=0)
    given_points_2 = models.IntegerField(default=0)
    is_published = models.IntegerField(default=0)
    decision = models.ForeignKey(Decision, related_name='decision', on_delete=models.CASCADE)

    ## tracking
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Discussion(models.Model):
    text = models.TextField()
    decision = models.ForeignKey(Decision, related_name='discussion_decision', on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    ##tracking
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return "{} vs {}".format(self.decision.name1, self.decision.name2)