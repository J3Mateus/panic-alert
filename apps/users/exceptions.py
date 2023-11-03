from django.core.exceptions import ValidationError

class SchoolNotFoundValidationError(ValidationError):
    pass

class RoleNotFoundValidationError(ValidationError):
    pass

class UserNotFoundValidationError(ValidationError):
    pass

class COPNotFoundValidationError(ValidationError):
    pass