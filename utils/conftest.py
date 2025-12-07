import os
import pytest
from datetime import datetime
from utils.driver_setup import create_driver
from utils.logger import logger
from pytest_html import extras as html_extras

@pytest.fixture
def driver(request):
    logger.info("Iniciando driver")
    driver = create_driver()
    yield driver
    logger.info("Cerrando driver")
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if not hasattr(report, "extras"):
        report.extras = []

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"reports/screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_name)

            # Agregar screenshot como EXTRA (imagen incrustada en HTML)
            report.extras.append(
                html_extras.image(file_name, name="screenshot")
            )


def pytest_html_report_title(report):
    report.title = "Reporte Completo"


def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["Suite UI + API con evidencias automáticas"])
