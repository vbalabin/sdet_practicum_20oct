import pytest
from selenium import webdriver
import google.googlepage as gp


class TestGoogleCalc():
    @pytest.fixture(autouse=True)
    def run_around_tests(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")
        yield
        self.driver.close()


    def test_001_algebraic_integers(self):
        """
        info: Проверка операций с целыми числами
        """
        test_obj = gp.GoogleAlgebraic(self.driver)
        test_obj.perform_actions_01()
        assert test_obj.get_memory_value() == '(1 + 2) × 3 - 40 ÷ 5 =', 'memory value has failed'
        assert test_obj.get_result_value() == '1', 'result value test has failed'


    def test_002_zero_div(self):
        """
        info: Проверка деления на ноль
        """
        test_obj = gp.GoogleZeroDiv(self.driver)
        test_obj.perform_actions_02()    
        assert test_obj.get_memory_value() == '6 ÷ 0 =', 'memory value has failed'
        assert test_obj.get_result_value() == 'Infinity', 'result value test has failed'


    def test_003_empty_input(self):
        """
        info: Проверка ошибки при отсутствии значения
        """
        test_obj = gp.GoogleEmpty(self.driver)
        test_obj.perform_actions_03()        
        assert test_obj.get_memory_value() == 'sin() =', 'memory value has failed'
        assert test_obj.get_result_value() == 'Error', 'result value test has failed' 
