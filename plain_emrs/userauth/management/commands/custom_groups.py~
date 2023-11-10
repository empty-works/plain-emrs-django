from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from userauth.models import AuthUser

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **options):
        # Create groups
        doctor_group, created = Group.objects.get_or_create(name='Doctors')
        clinical_staff_group, created = Group.objects.get_or_create(name='Clinical Staff')
        attending_physician_group, created = Group.objects.get_or_create(name='Attending Physicians')
        specialist_group, created = Group.objects.get_or_create(name='Specialists')
        administrative_staff_group, created = Group.objects.get_or_create(name='Administrative Staff')
        it_staff_group, created = Group.objects.get_or_create(name='IT Staff')
        system_admin_group, created = Group.objects.get_or_create(name='System Administrators')

        # Assign permissions to groups
        self.assign_permissions(doctor_group, ['view_patient_record', 'update_patient_record', 'view_patient_medical_history', 
                                               'update_medical_history', 'view_diagnoses', 'update_diagnoses', 
                                               'view_treatment_plans', 'update_treatment_plans', 'prescribe_medication', 
                                               'can_order_tests', 'document_clinical_notes'])

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully'))

    def assign_permissions(self, group, permission_codenames):
        content_type = ContentType.objects.get_for_model(AuthUser)

        for codename in permission_codenames:
            permission = Permission.objects.get(content_type=content_type, codename=codename)
            group.permissions.add(permission)
