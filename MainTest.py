# from lib import OpenCVUtils
from lib.HtmlReport import HTMLTestReport


#中代码字符串拼接后，再写入文件中
def startTest():
    print("开始测试")
    # OpenCVUtils.compareImg("./resources/obj.png", "./resources/test.png")

# 由此方法将C#中的参数传入python中
if __name__ == "__main__":
    import sys

    # if len(sys.argv) != 3:
    #     print("运行参数不对")
    #     sys.exit(1)
    #
    # text = sys.argv[1]


    # startTest()

    # 初始化报告
    report = HTMLTestReport(title="Automated Test Report",template_path="./",output_file="report.html")

    # 添加用例
    case1_id = report.add_test_case("Login Test", "Verify login functionality.")
    case2_id = report.add_test_case("Payment Test", "Verify payment processing.")

    # 向用例添加步骤
    report.add_test_step(case1_id, "Open login page.", "Pass")
    report.add_test_step(case1_id, "Enter valid credentials.", "Pass")
    report.add_test_step(case1_id, "Click login button.", "Fail")  # 此步骤失败，整个用例状态更新为 Fail

    report.add_test_step(case2_id, "Select product.", "Pass")
    report.add_test_step(case2_id, "Proceed to checkout.", "Pass")
    report.add_test_step(case2_id, "Enter payment details.", "Pass")

    # 完成报告
    report.complete()
