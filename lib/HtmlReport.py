import uuid
from jinja2 import Environment, FileSystemLoader

class HTMLTestReport:
    def __init__(self, title="Test Report", template_path="../", output_file="report.html"):
        self.title = title
        self.test_cases = []  # 存储测试用例信息
        self.output_file = output_file
        self.env = Environment(loader=FileSystemLoader(searchpath=template_path))
        self.template = self.env.get_template("report_templete.html")

    def add_test_case(self, name, description):
        """添加测试用例"""
        case_id = str(uuid.uuid4())
        self.test_cases.append({
            "id": case_id,
            "name": name,
            "description": description,
            "status": "Pending",  # 默认状态为 Pending
            "steps": []  # 初始化为空步骤列表
        })
        return case_id

    def add_test_step(self, case_id, description, status):
        """向指定用例添加测试步骤"""
        for case in self.test_cases:
            if case["id"] == case_id:
                case["steps"].append({
                    "description": description,
                    "status": status
                })
                # 更新用例状态
                case["status"] = self._update_case_status(case["steps"])
                break
        self._generate_html()

    def _update_case_status(self, steps):
        """根据步骤状态更新用例状态"""
        if any(step["status"] == "Fail" for step in steps):
            return "Fail"
        return "Pass"

    def _generate_html(self):
        """根据模板生成 HTML 文件"""
        html_content = self.template.render(title=self.title, test_cases=self.test_cases)
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(html_content)

    def complete(self):
        """完成报告"""
        print(f"Test report generated: {self.output_file}")
