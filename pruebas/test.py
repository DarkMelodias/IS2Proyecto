from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from pruebas_usr import TestServer

assertions_test = TestLoader().loadTestsFromTestCase(TestServer)

smoke_test = TestSuite(assertions_test)
kwargs = {
    "output": 'smoke-report'
    ,
    'report_name':'results'
}

runner = HTMLTestRunner(**kwargs)

runner.run(smoke_test)