from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# class FinanceUserManager(BaseUserManager):
#     def create_superuser(self, phone_number, **kwargs):
#         self.model.objects.create(phone_number=phone_number)


class FinanceUser(AbstractUser):
    # BORROWER = "BR"
    LENDER = "LR"

    USER_TYPES = (
        # (BORROWER, "User who borrow money from other"),
        (LENDER, "User who lends money to others with interest"),
    )
    phone_number = models.PositiveBigIntegerField(unique=True)
    user_type = models.CharField(max_length=15, choices=USER_TYPES, default=LENDER)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # objects = FinanceUserManager

    def __str__(self):
        return "Create User"


def content_file_name(instance, filename):
    return '/'.join(['content', instance.user.username, filename])


class AmountDetails(models.Model):
    lender = models.ForeignKey(FinanceUser, on_delete=models.DO_NOTHING, related_name="lender_borrower_mapping")
    amount = models.PositiveIntegerField(default=0)
    interest_rate = models.FloatField(default=0.75, help_text="Interest rate in rupees")
    interest_percentage = models.IntegerField(default=0)
    agreement_file = models.FileField(upload_to=content_file_name)
    lended_to = models.CharField(max_length=100)
    interest_amount = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    is_closed = models.BooleanField(default=False)
    lender_mobile_number = models.PositiveBigIntegerField(default=999999999)

    def __str__(self):
        return f"Lends Money to user {self.lended_to}"
