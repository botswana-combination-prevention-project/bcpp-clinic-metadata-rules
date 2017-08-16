from django.apps import AppConfig as DjangoApponfig
from django.conf import settings


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_metadata_rules'


if 'bcpp_clinic_metadata_rules' in settings.APP_NAME:
    from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig, SubjectType, Cap
    from datetime import datetime
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
    from edc_appointment.facility import Facility
    from dateutil.tz import gettz
    from edc_metadata.apps import AppConfig as MetadataAppConfig

    class EdcMetadataAppConfig(MetadataAppConfig):
        reason_field = {'bcpp_clinic_subject.subjectvisit': 'reason'}

    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP066'
        protocol_number = '066'
        protocol_name = 'BCPP Clinic'
        protocol_title = 'Botswana Combination Prevention Project'
        subject_types = [
            SubjectType('subject', 'Research Subject',
                        Cap(model_name='bcpp_clinic_subject.subjectconsent', max_subjects=9999)),
        ]
        study_open_datetime = datetime(
            2013, 10, 18, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 1, 0, 0, 0, tzinfo=gettz('UTC'))

        @property
        def site_name(self):
            return 'test_community'

        @property
        def site_code(self):
            return '01'
