from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Create custom groups and permissions'

    def handle(self, *args, **options):
        # Groups
        patient_group, created = Group.objects.get_or_create(name='Patients')
        doctor_provider_group, created = Group.objects.get_or_create(name='DoctorsProviders')
        attending_physician_group, created = Group.objects.get_or_create(name='AttendingPhysicians')
        specialist_group, created = Group.objects.get_or_create(name='Specialists')
        nurse_clinical_staff_group, created = Group.objects.get_or_create(name='NursesClinicalStaff')
        administrative_staff_group, created = Group.objects.get_or_create(name='AdministrativeStaff')
        system_admin_group, created = Group.objects.get_or_create(name='SystemAdministrators')

        # Permissions
        User = get_user_model()

        # Add new permissions here!
        view_patientlist_code = 'view_patientlist'
        view_patientlist_name = 'Permission to view patient list'

        custom_permissions = [
                {'codename': view_patientlist_code, 'name': view_patientlist_name},
        ]

        content_type = ContentType.objects.get_for_model(User)

        for permission_info in custom_permissions:
            permission, created = Permission.objects.get_or_create(
                    codename = permission_info['codename'],
                    name = permission_info['name'],
                    content_type = content_type,
            )

        # Add permissions to groups

