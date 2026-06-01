from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
def crear_admin(request):

    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            password='123456',
            email='admin@gmail.com'
        )

    return Response({"mensaje": "Admin creado"})