from definitions import TEMP_FOLDER
import logging
import shutil
import pytest
logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def cleanup():

    yield

    logger.info('!------------------------- cleanup -------------------------!')

    shutil.rmtree(TEMP_FOLDER, ignore_errors=True)