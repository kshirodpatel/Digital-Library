from django.db import models
from accounts.models import User

class Book(models.Model):
    FORMAT = (
        ('Hardcover', 'Hardcover'),
        ('Paperback', 'Paperback')
    )

    LANGUAGES = (
        ('English', 'English'),
        ('Spanish', 'Spanish'),
        ('French', 'French'),
        ('German', 'German'),
        ('Chinese', 'Chinese'),
        ('Japanese', 'Japanese'),
        ('Russian', 'Russian'),
        ('Arabic', 'Arabic'),
        ('Portuguese', 'Portuguese'),
        ('Italian', 'Italian'),
        ('Hindi', 'Hindi'),
        ('Korean', 'Korean'),
        ('Turkish', 'Turkish'),
        ('Bengali', 'Bengali'),
        ('Dutch', 'Dutch'),
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image_url = models.URLField(max_length=200, blank=True, null=True) 
    isbn = models.CharField(max_length=13, unique=True, help_text='13 Character ISBN')
    about = models.TextField()
    language = models.CharField(max_length=200, choices=LANGUAGES, default='English')
    format = models.CharField(max_length=200, choices=FORMAT, default='Paperback')
    published = models.DateField()
    category = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title}"

