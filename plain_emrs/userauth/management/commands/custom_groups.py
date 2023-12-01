from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from userauth.models import AuthUser

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **options):
        # Create groups
        self.create_groups()

        # Create or get permissions
        self.create_permissions()

        # Assign permissions to groups
        self.assign_perms_to_groups()

        # Display all groups and their permissions
        self.display_groups_permissions()

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully'))

    def create_groups(self):
        self.patient_group, created = Group.objects.get_or_create(name='Patients')
        self.doctor_group, created = Group.objects.get_or_create(name='Doctors')
        self.clinical_staff_group, created = Group.objects.get_or_create(name='Clinical Staff')
        self.attending_physician_group, created = Group.objects.get_or_create(name='Attending Physicians')
        self.specialist_group, created = Group.objects.get_or_create(name='Specialists')
        self.administrative_staff_group, created = Group.objects.get_or_create(name='Administrative Staff')
        self.it_staff_group, created = Group.objects.get_or_create(name='IT Staff')
        self.system_admin_group, created = Group.objects.get_or_create(name='System Administrators')

    def create_permissions(self):
        self.content_type = ContentType.objects.get_for_model(AuthUser)

        view_patient_record_permission, created = Permission.objects.get_or_create(
            codename='view_patient_record',
            name='Can view patient record',
            content_type=self.content_type,
        )

        update_demographic_info_permission, created = Permission.objects.get_or_create(
            codename='update_demographic_info',
            name='Can update patient\'s demographic info',
            content_type=self.content_type,
        )

        update_clinical_data_permission, created = Permission.objects.get_or_create(
            codename='update_clinical_data',
            name='Can update patient\'s clinical data',
            content_type=self.content_type,
        )

        view_patient_medical_history_permission, created = Permission.objects.get_or_create(
            codename='view_patient_medical_history',
            name='Can view patient\'s medical history',
            content_type=self.content_type,
        )

        update_medical_history_permission, created = Permission.objects.get_or_create(
            codename='update_medical_history',
            name='Can update patient\'s medical history',
            content_type=self.content_type,
        )

        can_contact_staff_permission, created = Permission.objects.get_or_create(
            codename='can_contact_staff',
            name='Can contact clinical staff',
            content_type=self.content_type,
        )

        access_system_configuration_permission, created = Permission.objects.get_or_create(
            codename='access_system_configuration',
            name='Can access system configuration',
            content_type=self.content_type,
        )

        access_maintenance_tools_permission, created = Permission.objects.get_or_create(
            codename='access_maintenance_tools',
            name='Can access maintenance tools',
            content_type=self.content_type,
        )

        view_logs_permission, created = Permission.objects.get_or_create(
            codename='view_logs',
            name='Can view logs',
            content_type=self.content_type,
        )

        view_demographic_info_permission, created = Permission.objects.get_or_create(
            codename='view_demographic_info',
            name='Can view patient\'s demographic info',
            content_type=self.content_type,
        )

        register_patient_permission, created = Permission.objects.get_or_create(
            codename='register_patient',
            name='Can register patient',
            content_type=self.content_type,
        )

        view_appointments_permission, created = Permission.objects.get_or_create(
            codename='view_appointments',
            name='Can view appointments',
            content_type=self.content_type,
        )

        schedule_appointments_permission, created = Permission.objects.get_or_create(
            codename='schedule_appointments',
            name='Can schedule appointments',
            content_type=self.content_type,
        )

        view_diagnoses_permission, created = Permission.objects.get_or_create(
            codename='view_diagnoses',
            name='Can view diagnoses',
            content_type=self.content_type,
        )

        update_diagnoses_permission, created = Permission.objects.get_or_create(
            codename='update_diagnoses',
            name='Can update diagnoses',
            content_type=self.content_type,
        )

        view_treatment_plans_permission, created = Permission.objects.get_or_create(
            codename='view_treatment_plans',
            name='Can view treatment plans',
            content_type=self.content_type,
        )

        update_treatment_plans_permission, created = Permission.objects.get_or_create(
            codename='update_treatment_plans',
            name='Can update treatment plans',
            content_type=self.content_type,
        )

        prescribe_medication_permission, created = Permission.objects.get_or_create(
            codename='prescribe_medication',
            name='Can prescribe medication',
            content_type=self.content_type,
        )

        can_order_tests_permission, created = Permission.objects.get_or_create(
            codename='can_order_tests',
            name='Can order tests',
            content_type=self.content_type,
        )

        document_clinical_notes_permission, created = Permission.objects.get_or_create(
            codename='document_clinical_notes',
            name='Can document clinical notes',
            content_type=self.content_type,
        )

        care_plan_approval_permission, created = Permission.objects.get_or_create(
            codename='care_plan_approval',
            name='Can approve a patient\'s care plans',
            content_type=self.content_type,
        )

        orders_approval_permission, created = Permission.objects.get_or_create(
            codename='orders_approval',
            name='Can approve orders',
            content_type=self.content_type,
        )

        prescribe_specialized_medication_permission, created = Permission.objects.get_or_create(
            codename='prescribe_specialized_medication',
            name='Can prescribe specialized medication',
            content_type=self.content_type,
        )

        authorize_device_implantation_permission, created = Permission.objects.get_or_create(
            codename='authorize_device_implantation',
            name='Can authorize device implantation',
            content_type=self.content_type,
        )

        access_security_settings_permission, created = Permission.objects.get_or_create(
            codename='access_security_settings',
            name='Can access security settings',
            content_type=self.content_type,
        )

        apply_updates_permission, created = Permission.objects.get_or_create(
            codename='apply_updates',
            name='Can apply system updates',
            content_type=self.content_type,
        )

    def assign_perms_to_groups(self):
        self.assign_permissions(self.patient_group, ['view_patient_record', 'update_demographic_info'])

        self.assign_permissions(self.clinical_staff_group, ['view_patient_record', 'update_demographic_info', 'update_clinical_data', 'view_patient_medical_history', 
                                                       'update_medical_history', 'can_contact_staff'])

        self.assign_permissions(self.it_staff_group, ['access_system_configuration', 'access_maintenance_tools', 'view_logs'])

        # view_patient_record includes all the following 'view' permissions
        self.assign_permissions(self.administrative_staff_group, ['view_demographic_info', 'update_demographic_info', 'register_patient', 'view_appointments', 'schedule_appointments'])

        # Specialized groups
        self.assign_permissions(self.doctor_group, ['view_diagnoses', 'update_diagnoses', 'view_treatment_plans', 'update_treatment_plans', 'prescribe_medication', 
                                               'can_order_tests', 'document_clinical_notes'])

        self.assign_permissions(self.attending_physician_group, ['care_plan_approval', 'orders_approval'])

        self.assign_permissions(self.specialist_group, ['prescribe_specialized_medication', 'authorize_device_implantation'])

        self.assign_permissions(self.system_admin_group, ['access_security_settings', 'apply_updates'])

    def assign_permissions(self, group, permission_codenames):

        for codename in permission_codenames:
            permission = Permission.objects.get(content_type=self.content_type, codename=codename)
            group.permissions.add(permission)
    
    def display_groups_permissions(self):
        self.stdout.write(self.style.SUCCESS('\nDisplaying Groups and Permissions:\n'))

        for group in Group.objects.all():
            self.stdout.write(self.style.SUCCESS(f'Group: {group.name}'))

            if group.permissions.exists():
                self.stdout.write(self.style.SUCCESS('  Permissions:'))

                for permission in group.permissions.all():
                    self.stdout.write(self.style.SUCCESS(f'    - {permission.codename}'))
            else:
                self.stdout.write(self.style.SUCCESS('  No permissions assigned'))

            self.stdout.write('\n')