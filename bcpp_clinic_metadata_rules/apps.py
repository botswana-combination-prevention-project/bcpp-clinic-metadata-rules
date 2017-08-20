from django.apps import AppConfig as DjangoApponfig
from django.conf import settings


class AppConfig(DjangoApponfig):
    name = 'bcpp_clinic_metadata_rules'


if settings.APP_NAME == 'bcpp_clinic_metadata_rules':
    from edc_metadata.apps import AppConfig as MetadataAppConfig

    class EdcMetadataAppConfig(MetadataAppConfig):
        reason_field = {'bcpp_clinic_metadata_rules.subjectvisit': 'reason'}
