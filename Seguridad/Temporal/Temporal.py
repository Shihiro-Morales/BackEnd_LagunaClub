from django.contrib.auth import get_user_model
from gunicorn.config import User
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def crear_admin(request):

    user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@gmail.com',
            'is_staff': True,
            'is_superuser': True,
        }
    )

    user.set_password('123456')
    user.is_active = True
    user.save()

    return Response({
        "created": created,
        "username": user.username,
        "is_active": user.is_active
    })