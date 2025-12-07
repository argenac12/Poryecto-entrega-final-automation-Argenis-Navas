import logging
import pathlib

log_dir = pathlib.Path("logs")
log_dir.mkdir(exist_ok=True)

logging.basicConfig(
    filename=log_dir / "suite.log",
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt='%H:%M:%S'
)

logger = logging.getLogger("framework")