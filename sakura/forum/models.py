from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=20, default='null')


class Topic(models.Model):
    topic_name = models.CharField(max_length=200)
    topic_description = models.TextField()
    topic_creator = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creation_time = models.DateTimeField('creation time', auto_now_add=True)
    likes = models.ManyToManyField(Customer, related_name="like", blank=True)
    dislikes = models.ManyToManyField(Customer, related_name="dislike")

    @classmethod
    def create(cls, topic_name, topic_description):
        topic = cls(topic_name=topic_name, topic_description=topic_description)
        topic.topic_creator = Customer.objects.get(pk=1)
        return topic


class Thread(models.Model):
    thread_content = models.TextField()
    thread_creator = models.ForeignKey(Customer, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    @classmethod
    def create(cls, topic, thread_content, thread_creator):
        thread = cls(topic=topic, thread_content=thread_content,
                     thread_creator=thread_creator)
        thread.like = 0
        thread.dislike = 0
        return thread
