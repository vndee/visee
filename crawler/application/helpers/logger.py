import logging
from logging import handlers
import sys
from datetime import date
import os

root_dir = 'logs/'
try:
    os.mkdir(root_dir)
except:
    pass


def get_logger(log_name, max_log_file_in_mb=15, logger_name='default'):
    """
    Get logging and format
    All logs will be saved into logs/log-DATE (default)
    Default size of log file = 15m
    :param log_name:
    :param max_log_file_in_mb:
    :param logger_name:
    :return:
    """
    log = logging.getLogger(logger_name)
    log.setLevel(logging.DEBUG)
    log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(log_format)
    log.addHandler(ch)

    fh = handlers.RotatingFileHandler(log_name + '-' + str(date.today()),
                                      maxBytes=(1024*1024)*max_log_file_in_mb,
                                      backupCount=7)
    fh.setFormatter(log_format)
    log.addHandler(fh)

    return log


info_log = get_logger(root_dir + 'info.log', 25, logger_name='info')
error_log = get_logger(root_dir + 'error.log', 25, logger_name='error')
