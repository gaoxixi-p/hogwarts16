def setup_function():
    #setup 在每个方法前执行一次
    print("资源准备：setup function")
def teardown_function():
    print("资源销魂：teardown function")

def test_case1():
    print("case1")

def test_case2():
    print("case2")
def setup_function():
    #setup 在每个方法前执行一次
    print("资源准备：setup function")
def teardown_function():
    print("资源销魂：teardown function")
class TestDemo:
    #setup_class 是在整个类开始和结束分别执行一次
    def setup_class(self):
        print("类资源准备：TestDemo setup_class")
    def test_demo1(self):
        print("test demo1")
    def test_demo2(self):
        print("test demo2")
    def teardown_class(self):
        print("类资源结束TestDemo teardown")

#模块级别
def setup_module():
    print("资源准备模块 setup")
def test_demo2():
    print("test demo2")
def test_demo3():
    print("test demo3")
def teardown_module():
    print("资源结束模块 teardown")
def test_demo3():
    print("test demo3")