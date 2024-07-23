from django.utils import timezone


def soft_delete(instance):
    instance.is_deleted = True
    instance.deleted_at = timezone.now()
    instance.save()