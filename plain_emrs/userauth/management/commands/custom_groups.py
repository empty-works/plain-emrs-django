from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from userauth.models import AuthUser

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **options):
        # Create groups
        patient_group, created = Group.objects.get_or_create(name='Patients')
        doctor_group, created = Group.objects.get_or_create(name='Doctors')
        clinical_staff_group, created = Group.objects.get_or_create(name='Clinical Staff')
        attending_physician_group, created = Group.objects.get_or_create(name='Attending Physicians')
        specialist_group, created = Group.objects.get_or_create(name='Specialists')
        administrative_staff_group, created = Group.objects.get_or_create(name='Administrative Staff')
        it_staff_group, created = Group.objects.get_or_create(name='IT Staff')
        system_admin_group, created = Group.objects.get_or_create(name='System Administrators')

        # Shared permissions
        view_patient_record = 'view_patient_record'
        update_demographic_info = 'update_demographic_info'

        # Assign permissions to groups

        # Common groups
        self.assign_permissions(patient_group, [view_patient_record, update_demographic_info])

        self.assign_permissions(clinical_staff_group, [view_patient_record, update_demographic_info, 'update_clinical_data', 'view_patient_medical_history', 
                                                       'update_medical_history', 'can_contact_staff'])

        self.assign_permissions(it_staff_group, ['access_system_configuration', 'access_maintenance_tools', 'view_logs'])

        # view_patient_record includes all the following 'view' permissions
        self.assign_permissions(administrative_staff_group, ['view_demographic_info', update_demographic_info, 'register_patient', 'view_appointments', 'schedule_appointments'])

        # Specialized groups
        self.assign_permissions(doctor_group, ['view_diagnoses', 'update_diagnoses', 'view_treatment_plans', 'update_treatment_plans', 'prescribe_medication', 
                                               'can_order_tests', 'document_clinical_notes'])

        self.assign_permissions(attending_physician_group, ['care_plan_approval', 'orders_approval'])

        self.assign_permissions(specialist_group, ['prescribe_specialized_medication', 'authorize_device_implantation'])

        self.assign_permissions(system_admin_group, ['access_security_settings', 'apply_updates'])


        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully'))

    def assign_permissions(self, group, permission_codenames):
        content_type = ContentType.objects.get_for_model(AuthUser)

        for codename in permission_codenames:
            permission = Permission.objects.get(content_type=content_type, codename=codename)
            group.permissions.add(permission)
