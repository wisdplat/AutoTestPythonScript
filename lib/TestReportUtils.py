from lib.HtmlReport import TestReport
from lib.ReportIO import ReportIO


def startRecord():
    report = ReportIO._instance
    report.reportIn("test")
    tr = TestReport(title="测试")
    tr.log_step("测试111", "Fail", None)

def generateReport(reportFile):
    """
    生成测试报告
    :param reportFile: “Excel”,"Html"
    :return: path 生成报告路径
    """
    print("生成报告")