from bcpp_clinic_labs.labs import panel_rbd, panel_vl
from edc_constants.constants import OTHER
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule, RequisitionRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.decorators import register
from edc_metadata.rules.predicate import P
from edc_metadata.rules.requisition import RequisitionRuleGroup

from ..constants import MASA_VL_SCHEDULED, INITIATION

app_label = 'bcpp_clinic_subject'


@register()
class QuestionnaireCrfRuleGroup(CrfRuleGroup):

    viralloadtracking = CrfRule(
        predicate=P('registration_type', 'eq', MASA_VL_SCHEDULED),
        consequence=REQUIRED,
        alternative=NOT_REQUIRED,
        target_models=[f'{app_label}.viralloadtracking'])

    viralloadtracking1 = CrfRule(
        predicate=P('registration_type', 'eq', OTHER),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=[f'{app_label}.viralloadtracking'])

    viralloadtracking2 = CrfRule(
        predicate=P('registration_type', 'eq', INITIATION),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=[f'{app_label}.viralloadtracking'])

    class Meta:
        source_model = f'{app_label}.questionnaire'
        app_label = 'bcpp_clinic_metadata_rules'


@register()
class QuestionnaireRequisitionRuleGroup(RequisitionRuleGroup):

    initiation = RequisitionRule(
        predicate=P('registration_type', 'eq', MASA_VL_SCHEDULED),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_panels=[panel_vl],)

    class Meta:
        source_model = 'bcpp_clinic_subject.questionnaire'
        requisition_model = f'{app_label}.subjectrequisition'
        app_label = 'bcpp_clinic_metadata_rules'
