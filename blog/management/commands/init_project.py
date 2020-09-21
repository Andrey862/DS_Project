from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
from blog.models import Post
from random import choice

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            admin = User.objects.create_superuser(username='admin', password='admin')
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            user = User.objects.create_user(username='user1', password='qwerty')
            user.is_active = True
            user.save()
            user = User.objects.create_user(username='user2', password='qwerty')
            user.is_active = True
            user.save()
            user = User.objects.create_user(username='user3', password='qwerty')
            user.is_active = True
            user.save()
        if (Post.objects.count() == 0):
            fake=Faker()
            users= list(User.objects.all())
            for i in range(100):
                text = fake.paragraph(nb_sentences=40)
                title = fake.sentence(nb_words=3)
                date = fake.date_between(start_date='-60d', end_date='+0d')
                user = choice(users)
                Post.objects.create(
                    title = title,
                    content = text,
                    date_posted = date,
                    author = user
                )
        
        
