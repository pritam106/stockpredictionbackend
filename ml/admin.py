from django.contrib.auth.models import User
u = User.objects.get(username='admin')
u.set_password('123456')
u.save()