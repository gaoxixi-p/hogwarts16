import pytest

from pythcode.calculator import Calculator

#测试方法写的正确性，需要先把类名实例化，才可以调用方法
# class TestCalc:
#     def setup_class(self):
#         #self.calc  加slef变成类的实例变量
#         self.calc=Calculator()
#         print("计算开始")
#     def teardown_class(self):
#         print("计算结束")
#     def test_add(self):
#         # calc=Calculator()
#         result=self.calc.add(1,1)
#         assert result==2
#     def test_add1(self):
#         # calc=Calculator()
#         result=self.calc.add(10,1)
#         assert result==11
#     def test_add3(self):
#         # calc=Calculator()
#         result=self.calc.add(100,100)
#         assert result==200

#参数化 加法
class TestCalc:
    def setup_class(self):
        #self.calc  加slef变成类的实例变量
        self.calc=Calculator()
        print("计算开始")
    def teardown_class(self):
        print("计算结束")
    @pytest.mark.parametrize('a,b,expect',[[1,1,2],[20,1,21],[1000,100,1100],[-100,-50,-150]],ids=['int_case','mid_case','big_case','fudate'])
    def test_add(self,a,b,expect):
        # calc=Calculator()
        result=self.calc.add(a,b)
        assert result==expect
#参数化除法
    @pytest.mark.parametrize('a,b,expect',[[-6,3,-2],[1,2,0.5],[100,5,20],[0,10,0],[100,0,"na"]],ids=['fu_case','small','big','zero','hotbig'])
    def test_div(self,a,b,expect):
        result=self.calc.div(a,b)
        assert  result==expect
