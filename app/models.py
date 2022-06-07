from django.db import models

from django.db import models
from django.contrib.auth.models import User

BOOK_CATEGORY = (
    ('Motivational', 'Motivational'),
    ('Biography', 'Biography'),
    ('Autobiography', 'Autobiography'),
    ('Kids', 'Kids'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other')

)


class book(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    category = models.CharField(choices=BOOK_CATEGORY, max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book_data'


class LoginInfo_Table(models.Model):
    email=models.EmailField(max_length=20,unique=True)
    name=models.CharField(max_length=30)
    passwd=models.CharField(max_length=20)

    def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)

    class Meta:
        unique_together=('email','passwd')
        db_table = 'Login_Info'



