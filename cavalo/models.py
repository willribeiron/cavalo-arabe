from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Users(BaseModel):
    allowed_to_receive_stamps = models.BooleanField(default=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Campaign(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    stamp_quantity = models.IntegerField(blank=False)


class Card(BaseModel):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)


class Stamp(BaseModel):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    received_date = models.DateField(auto_now_add=True)


class Bonus(BaseModel):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bonus'
        verbose_name_plural = 'Bonus'
