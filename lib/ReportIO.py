from rx.subject import Subject

# 创建公共流
public_stream = Subject()

# 定义订阅者
def subscriber(value):
    print(f"Subscriber received: {value}")

public_stream.subscribe(subscriber)

# 定义生产者函数
def producer_1():
    public_stream.on_next("Producer 1: Hello")

def producer_2():
    public_stream.on_next("Producer 2: World")

# 不同地方调用生产者
producer_1()
producer_2()

