from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication as OriginalJWTAuthentication
from rest_framework_simplejwt.settings import api_settings
from rest_framework.authentication import CSRFCheck
from rest_framework.exceptions import PermissionDenied


def enforce_csrf(request):
    """
    Enforce CSRF validation.
    """
    check = CSRFCheck()
    # populates request.META['CSRF_COOKIE'], which is used in process_view()
    check.process_request(request)
    request.META[settings.CSRF_HEADER_NAME] = request.META.get("CSRF_COOKIE")
    reason = check.process_view(request, None, (), {})
    if reason:
        # CSRF failed, bail with explicit error message
        raise PermissionDenied("CSRF Failed: %s" % reason)


class JWTAuthentication(OriginalJWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            if not api_settings.AUTH_COOKIE:
                return None
            else:
                raw_token = request.COOKIES.get(api_settings.AUTH_COOKIE) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        user = self.get_user(validated_token)
        if not user or not user.is_active:
            return None

        if api_settings.AUTH_COOKIE:
            enforce_csrf(request)

        return user, validated_token
