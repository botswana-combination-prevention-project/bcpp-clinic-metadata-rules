from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.decorators import register
from edc_metadata.rules.predicate import P

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
        app_label = 'bcpp_clinic_metadata_rules'
