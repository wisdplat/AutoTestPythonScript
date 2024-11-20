import os
import time
from datetime import datetime

class TestReport:
    def __init__(self, title):
        self.title = title
        self.start_time = datetime.now()
        self.steps = []  # 保存测试步骤的记录

    def log_step(self, step_description, status="PASSED", error=None):
        """
        记录测试步骤
        :param step_description: 步骤描述
        :param status: 步骤状态，默认 "PASSED" 或 "FAILED"
        :param error: 如果失败，记录错误信息
        """
        step = {
            "description": step_description,
            "status": status,
            "error": error,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.steps.append(step)
        print(f"{step['timestamp']} - {step['description']} - {step['status']}")

    def generate_html_report(self, file_path):
        """
        生成 HTML 格式的测试报告
        :param file_path: 输出的文件路径
        """
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()

        # 创建 HTML 报告内容
        html = f"""
        <html>
        <head>
            <title>{self.title}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f4f4f4; }}
                .passed {{ color: green; }}
                .failed {{ color: red; }}
            </style>
        </head>
        <body>
            <h1>Test Report: {self.title}</h1>
            <p>Start Time: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>End Time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>Duration: {duration:.2f} seconds</p>
            <table>
                <tr>
                    <th>#</th>
                    <th>Description</th>
                    <th>Status</th>
                    <th>Error</th>
                    <th>Timestamp</th>
                </tr>
        """

        for i, step in enumerate(self.steps, start=1):
            status_class = "passed" if step["status"] == "PASSED" else "failed"
            error_msg = step["error"] if step["error"] else "-"
            html += f"""
                <tr>
                    <td>{i}</td>
                    <td>{step['description']}</td>
                    <td class="{status_class}">{step['status']}</td>
                    <td>{error_msg}</td>
                    <td>{step['timestamp']}</td>
                </tr>
            """

        html += """
            </table>
        </body>
        </html>
        """

        # 写入文件
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Test report generated: {file_path}")
