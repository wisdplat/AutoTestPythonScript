from lib import OpenCVUtils
from lib.HtmlReport import TestReport

#中代码字符串拼接后，再写入文件中
def startTest():
    print("开始测试")
    OpenCVUtils.compareImg("./resources/obj.png", "./resources/test.png")





# 由此方法将C#中的参数传入python中
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("运行参数不对")
        sys.exit(1)

    text = sys.argv[1]
    tr = TestReport(title="测试")
    tr.log_step("测试111", "Fail", None)

    startTest()
    tr.generate_html_report("./test.html")

