from scanner.scanner import Scanner
import config.logger
import logging
import os

logger = logging.getLogger(__name__)

scanner = Scanner()
network = os.environ.get("NETWORK")
logger.info(f"{network=}")

scanner.ping_scan(network)
scanner.ssh_scan(network)
