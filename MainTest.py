# from lib import OpenCVUtils
import importlib.util
import os

from lib.AudioToText import getAudio
from lib.HtmlReport import HTMLTestReport


#中代码字符串拼接后，再写入文件中
def startTest():
    print("开始测试")
    # OpenCVUtils.compareImg("./resources/obj.png", "./resources/test.png")
    getAudio("test.wav")


def load_local_module(module_path, method_name=None):
    """动态加载本地模块并调用指定方法"""
    # 获取模块名（文件名去掉扩展名）
    module_name = os.path.splitext(os.path.basename(module_path))[0]

    # 加载模块
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None:
        raise ImportError(f"Could not load module from path: {module_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module  # 将模块添加到 sys.modules 中
    spec.loader.exec_module(module)  # 执行模块代码

    print(f"Module '{module_name}' loaded successfully.")

    # 如果指定了方法名，调用方法
    if method_name:
        try:
            method = getattr(module, method_name)
            return method
        except AttributeError:
            raise AttributeError(f"Method '{method_name}' not found in module '{module_name}'")

    return module

# 由此方法将C#中的参数传入python中
if __name__ == "__main__":
    import sys

    # if len(sys.argv) != 3:
    #     print("运行参数不对")
    #     sys.exit(1)
    #
    # text = sys.argv[1]


    # startTest()
    #
    # # 初始化报告
    # report = HTMLTestReport(title="Automated Test Report",template_path="./",output_file="report.html")
    #
    # # 添加用例
    # case1_id = report.add_test_case("Login Test", "Verify login functionality.")
    # case2_id = report.add_test_case("Payment Test", "Verify payment processing.")
    #
    # # 向用例添加步骤
    # report.add_test_step(case1_id, "Open login page.", "Pass")
    # report.add_test_step(case1_id, "Enter valid credentials.", "Pass")
    # report.add_test_step(case1_id, "Click login button.", "Fail")  # 此步骤失败，整个用例状态更新为 Fail
    #
    # report.add_test_step(case2_id, "Select product.", "Pass")
    # report.add_test_step(case2_id, "Proceed to checkout.", "Pass")
    # report.add_test_step(case2_id, "Enter payment details.", "Pass")

    # 完成报告
    # report.complete()

    # 加载python文件
    module_path = os.path.join(os.getcwd(), "case\\Test.py")
    # module = load_local_module(module_path)
    greet_function = load_local_module(module_path, "test")
    # 执行python文件中的方法
    greet_function()



