from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

"""
books = [
    {"Harry Potter 1 - The Philosopher's Stone", "J.K. Rowling", 5, True},
    {"Lord of the Rings", "J.R.R. Tolkien", 4, True}
]

For example:
    * Book.objects.get() return a single object so make sure that the parameter or criteria you put in get method must retrieve only one or no object
    * Book.objects.filter() return a list of objects according to the parameter you put into it. Never write : Book.objects.filter(rating<5), ... but there is another syntax to do that
    * Book.objects.filter(rating__lt = 4)
        - __lt          =>  lower than
        - __lte         =>  lower than or equal
        - __gt          =>  greater than
        - __gte         =>  greater than or equal
        - __exact       =>  == (case sensitive)
        - __iexact      =>  ILIKE '%value%' (not case sensitive)
        - __in          =>  IN in SQL query statement
        - __contains    =>  LIKE '%value%' (case sensitive)
        - __icontains   =>  LIKE '%value%' (not case sensitive)
        - __startswith  =>  LIKE 'value%' (case sensitive)
        - __istartwith  =>  LIKE 'value%' (not case sensitive)
        - __endwith     =>  LIKE '%value' (vase sensitive)
        - __iendwith    =>  LIKE '%value' (not case sensitive)
        - __range       =>  BETWEEN in SQL query statement
        - ...

    * Conditional query (or, and)
        make this import : from django.db.models import Q
        Example: - Book.objects.filter(Q(rating__lt = 3) | Q(is_bestselling = True))
                 - Book.objects.filter(Q(rating__lt = 3) | Q(is_bestselling = True), Q(author = "J.K. Rowling"))
                 - Book.objects.filter(Q(rating__lt = 3) | Q(is_bestselling = True), author = "J.K. Rowling")
        - So '|' for OR condition and ',' for AND condition
        - All queries rapped in Q() must come before those not rapped
        Example: - Book.objects.filter(author = "J.K. Rowling", Q(rating__lt = 3) | Q(is_bestselling = True)). This query won't work
"""

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null = True)
    """
    * CASCADE : every books related to this author will be deleted automatically
    * PROTECTED : avoid deleting author who is related to an existing book
    * SET : set a default value this specific author field when this specific author is deleted
    * SET_NULL : set NULL the value of author field when this one is deleted
    """
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, null=False, db_index=True)
    
    """
    - default : default value,
    - blank (True/False) : the object can be saved with/without any value
    - null (True/False) : the object can be saved with/without a NULL value
    - db_index (True/False) : Creating an index on this specific column
    - editable (True/False) : Specify if this field can be editable in the admin panel or not
    """

    def get_absolute_url(self):
        return reverse("book", args=[self.slug])   # type: ignore

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.rating})"