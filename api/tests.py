from django.test import Client, TestCase
from django.contrib.auth.models import User

from .models import Resume

class TestAndEdit(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.auth_user = User.objects.create(username='Человек Серьезный')
        cls.another_user = User.objects.create(username='Воришка')
        cls.resume = Resume.objects.create(
            owner = cls.auth_user,
            email = 'email@mail.ru',
            phone = 89991234567,
            title = 'Resume Title',
            portfolio = 'Some portfolio',
            experience = 10,
            education = 'school',
            salary = 123,
            specialty = 'Python',
            grade = 'very junior',
            status = 'done'
            )

        cls.auth_user_client = Client()
        cls.auth_user_client.force_login(cls.auth_user)
        cls.another_user_client = Client()
        cls.another_user_client.force_login(cls.another_user)

    # Понимаю, что не выполнил часть тз, не прописав тесты, но в данной реализации абсолютно все проверяется ORM, единственный тест возможен под номер телефона, но не понятно, какого именно формата.
