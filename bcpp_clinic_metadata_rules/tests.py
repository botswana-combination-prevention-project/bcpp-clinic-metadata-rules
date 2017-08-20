# from django.test import TestCase
# from arrow.arrow import Arrow
# from datetime import datetime
#
# from edc_constants.constants import NEG, POS, YES, NO, MALE, FEMALE
# from edc_constants.constants import YES, POS, NO, OTHER
# from edc_metadata.constants import REQUIRED, NOT_REQUIRED
# from edc_metadata.models import RequisitionMetadata, CrfMetadata
# from edc_reference import LongitudinalRefset
# from edc_reference.tests import ReferenceTestHelper
# from edc_registration.models import RegisteredSubject
#
# from .constants import (
#     INITIATION, VIRAL_LOAD, MASA_VL_SCHEDULED, RESEARCH_BLOOD_DRAW)
#
#
# class TestRuleGroups(TestCase):
#
#     reference_helper_cls = ReferenceTestHelper
#     visit_model = 'bcpp_clinic_subject.subjectvisit'
#     reference_model = 'edc_reference.reference'
#     report_datetime = Arrow.fromdatetime(
#         datetime(2015, 1, 7)).datetime
#     visit_code = 'C0'
#
#     def setUp(self):
#         self.subject_identifier = '111111111'
#         self.reference_helper = self.reference_helper_cls(
#             visit_model='bcpp_clinic_subject.subjectvisit',
#             subject_identifier=self.subject_identifier)
#
#         report_datetime = Arrow.fromdatetime(
#             datetime(2015, 1, 7)).datetime
#         self.reference_helper.create_visit(
#             report_datetime=report_datetime, timepoint='C0')
#
#     @property
#     def subject_visits(self):
#         return LongitudinalRefset(
#             subject_identifier=self.subject_identifier,
#             visit_model=self.visit_model,
#             model=self.visit_model,
#             reference_model_cls=self.reference_model
#         ).order_by('report_datetime')
#
#     def test_clinic_viral_load_required(self):
#         """Assert viral load is required if registration type is INITIATION.
#         """
#         self.reference_helper_cls(visit_model=self.visit_model, subject_identifier=self.subject_identifier).create_for_model(
#             report_datetime=self.report_datetime,
#             model='questionnaire',
#             visit_code=self.visit_code,
#             registration_type=INITIATION)
#
#         reqs = RequisitionMetadata.objects.filter(
#             subject_identifier=self.subject_identifier,
#             panel_name=VIRAL_LOAD,
#             entry_status=REQUIRED)
#         self.assertEqual(reqs.count(), 1)
#
#     def test_clinic_viral_load_required1(self):
#         """Assert viral load is required if registration type is OTHER.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='questionnaire',
#             visit_code=self.visit_code,
#             registration_type=OTHER)
#
#         reqs = RequisitionMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             panel_name=VIRAL_LOAD,
#             entry_status=REQUIRED)
#         self.assertEqual(reqs.count(), 1)
#
#     def test_clinic_viral_load_not_required(self):
#         """Assert viral load not required if not initiation or other.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='questionnaire',
#             visit_code=self.visit_code,
#             registration_type=MASA_VL_SCHEDULED)
#
#         reqs = RequisitionMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             panel_name=VIRAL_LOAD,
#             entry_status=NOT_REQUIRED)
#         self.assertEqual(reqs.count(), 1)
#
#     def test_clinic_rbd_required(self):
#         """Assert viral load not required if not initiation or other.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='questionnaire',
#             visit_code=self.visit_code,
#             registration_type=MASA_VL_SCHEDULED)
#
#         reqs = RequisitionMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             panel_name=RESEARCH_BLOOD_DRAW,
#             entry_status=REQUIRED)
#         self.assertEqual(reqs.count(), 1)
#
#     def test_clinic_vlloadtracking(self):
#         """Assert viralloadtracking is required on registration type is
#         MASA_VL_SCHEDULED.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='questionnaire',
#             visit_code=self.visit_code,
#             registration_type=MASA_VL_SCHEDULED)
#
#         crf = CrfMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             model='bcpp_clinic_subject.viralloadtracking',
#             entry_status=REQUIRED)
#         self.assertEqual(crf.count(), 1)
#
#     def test_clinic_vlloadtracking1(self):
#         """Assert viralloadtracking not required if not MASA_VL_SCHEDULED.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='questionnaire',
#             visit_code=self.visit_code,
#             registration_type=OTHER)
#
#         crf = CrfMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             model='bcpp_clinic_subject.viralloadtracking',
#             entry_status=NOT_REQUIRED)
#         self.assertEqual(crf.count(), 1)
#
#     def test_clinic_vl_result(self):
#         """Assert vlresult is required on is_drawn is YES.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='viralloadtracking',
#             visit_code=self.visit_code,
#             is_drawn=YES)
#
#         crf = CrfMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             model='bcpp_clinic_subject.vlresult',
#             entry_status=REQUIRED)
#         self.assertEqual(crf.count(), 1)
#
#     def test_clinic_vl_result1(self):
#         """Assert vlresult not required on is_drawn is NO.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='viralloadtracking',
#             visit_code=self.visit_code,
#             is_drawn=NO)
#
#         crf = CrfMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             model='bcpp_clinic_subject.vlresult',
#             entry_status=NOT_REQUIRED)
#         self.assertEqual(crf.count(), 1)
#
#     def test_clinic_viral_load1(self):
#         """Assert viralload required on is_drawn is YES.
#         """
#         self.reference_helper.create_for_model(
#             report_datetime=self.report_datetime,
#             model='viralloadtracking',
#             visit_code=self.visit_code,
#             is_drawn=YES)
#
#         crf = CrfMetadata.objects.filter(
#             subject_identifier=self.subject_visit.subject_identifier,
#             model='bcpp_clinic_subject.vlresult',
#             entry_status=REQUIRED)
#         self.assertEqual(crf.count(), 1)
