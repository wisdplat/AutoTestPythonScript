from lib.HtmlReport import HTMLTestReport

report:HTMLTestReport = None

def startRecord(title, template_path, output_file):
    global report
    report = HTMLTestReport(title, template_path, output_file)

def addCase(name, description):
    report.add_test_case(name, description)

def addCaseStepResult(case_id, description, status):
    report.add_test_step(case_id, description, status)

def generateReport(reportFile):
    """
    生成测试报告
    :param reportFile: “Excel”,"Html"
    :return: path 生成报告路径
    """
    print("生成报告")
    report.complete()