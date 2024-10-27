from django.db import models
from django.core.validators import RegexValidator      
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Users(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$')]
    )
    email = models.EmailField(unique=True, max_length=255)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = 'users'


class Books(models.Model):
    book_name = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    genre = models.CharField(max_length=225, null=False)
    published_on = models.DateField()
    add_by = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='added_books')
    is_borrowed = models.BooleanField(default=False)
    borrowed_by = models.ForeignKey(Users,on_delete=models.CASCADE, null=True, blank=True, related_name='borrowed_by')
    
    def __str__(self) -> str:
        return self.book_name + "-" + self.author 

    class Meta:
        db_table = 'books'