from django.db.models import QuerySet


class DevicesQuerySet(QuerySet):
    """Devices queryset."""

    def filter_by_user(self, user):

        if not user:
            return self.none()

        if user.is_admin is True:
            return self

        return self.filter(owners__id=user.id)
