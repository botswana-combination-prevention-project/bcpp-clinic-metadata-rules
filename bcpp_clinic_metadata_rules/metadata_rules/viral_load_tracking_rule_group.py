from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata_rules import CrfRuleGroup, CrfRule, register
from edc_metadata_rules import P

app_label = 'bcpp_clinic_subject'


@register()
class ViralLoadTrackingCrfRuleGroup(CrfRuleGroup):

    is_drawn = CrfRule(
        predicate=P('is_drawn', 'eq', YES),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.vlresult'])

    class Meta:
        source_model = f'{app_label}.viralloadtracking'
        app_label = app_label
