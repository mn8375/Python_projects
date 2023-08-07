import unittest

import HtmlTestRunner

from test_alerts import TestAlerts
from test_elefant_site import TestElefant
from test_login import TestLogin


class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests = unittest.TestSuite()
        tests.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestElefant)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title='first report', report_name='second_report')
        runner.run(tests)

