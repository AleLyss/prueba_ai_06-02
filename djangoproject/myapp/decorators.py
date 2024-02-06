from functools import wraps
from django.http import HttpResponseForbidden

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            profile = request.user.profile  # Asumiendo que el perfil del usuario está relacionado con User
            if profile.rol in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("Acceso denegado")
        return wrapper
    return decorator
