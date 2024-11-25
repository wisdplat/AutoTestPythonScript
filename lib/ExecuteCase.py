import importlib
import os
import sys


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

def run(file_path,method_name):
    # 加载python文件
    module_path = os.path.join(os.getcwd(), file_path)
    # module = load_local_module(module_path)
    greet_function = load_local_module(module_path, method_name)
    # 执行python文件中的方法
    greet_function()