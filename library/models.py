from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    username = models.CharField(max_length=50, null=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, validators=[RegexValidator(r'^\+?1?\d{9,15}$')])
    email = models.EmailField(unique=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.username
    
    class Meta:
        db_table = 'users'


class Books(models.Model):
    book_name = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=225, null=False)
    published_on = models.DateField()
    add_by = models.ForeignKey(Users, on_delete=models.DO_NOTHING, related_name='added_books')
    is_borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(Users,on_delete=models.DO_NOTHING, null=True, blank=True, related_name='borrowed_by')
    
    def __str__(self) -> str:
        return self.book_name + "-" + self.author 

    class Meta:
        db_table = 'books'