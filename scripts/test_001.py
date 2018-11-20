import allure,pytest
class Test_001:
    # @allure.step(title="步骤一")
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test__001_001(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    def test__001_006(self):
        assert False
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test__001_002(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    def test__001_003(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test__001_004(self):
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test__001_005(self):
        assert True

