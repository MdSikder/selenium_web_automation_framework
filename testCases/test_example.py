import pytest
from src.pages.example_page import ExamplePage
from src.utilities.logger import LogGen
from src.utilities.capture_screenshot import capture_screenshot

logger = LogGen.loggen()


class TestExample:
    @pytest.fixture(scope="class")
    def setup(self, request, env):
        self.page = ExamplePage(env=env)
        request.cls.page = self.page
        yield
        self.page.close_browser()

    @pytest.mark.smoke
    @pytest.mark.usefixtures("setup")
    def test_example(self):
        logger.info("Starting test_example")
        try:
            text = self.page.get_example_text()
            assert text == "Expected Text"
            logger.info("test_example passed")
        except AssertionError as e:
            capture_screenshot(self.page.driver, "test_example")
            logger.error(f"test_example failed: {e}")
            raise
