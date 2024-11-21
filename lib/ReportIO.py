from rx.subject import Subject

from libs.rich.diagnose import report

class ReportIO:
    # 创建公共流
    report_stream = Subject()
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    # 定义订阅者
    def subscriber(value):
        # TODO: 实现
        print(f"Subscriber received: {value}")

    def __init__(self):
        super().__init__()

        self.report_stream.subscribe(self.subscriber)

    def reportIn(self, message):
        self.report_stream.on_next(message)


