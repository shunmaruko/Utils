import argparse
import logging
import time
import sys

from .paths import REPOSITORY_DIRECTORY, create_paths

logger = logging.getLogger(__name__)

class LogSettings:
    def __init__(self, numeric_level):
        self.__numeric_level = numeric_level

    @property
    def numeric_level(self) -> int:
        return self.__numeric_level

def _get_loglevel() -> int:
    """ get loglevel from command line argment
    Return:
        numeric_level(int):Number assined to each logging level 
                           See https://docs.python.org/ja/3/library/logging.html?highlight=logging%20debug
        
    """
    parser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
            )
    group=parser.add_mutually_exclusive_group()
    group.add_argument(
            "-l", 
            "--log", 
            type=str,
            help="Assuming loglevel is bound to the string value obtained from the  \
            command line argument. Convert to upper case to allow the user to  \
            specify --log=DEBUG or --log=debug",
            default="WARNING", 
            choices=["DEBUG", "debug", "INFO", "info", "WARNING", "warning", "ERROR", "error", "CRITICAL", "critical"]
            )
    group.add_argument(
            "-v", 
            "--verbosity",
            help="increase output verbosity",
            default=0, 
            action="count"
            )
    args=parser.parse_args()
    numeric_level= getattr(logging, args.log.upper(), None)
    return numeric_level 

def _add_stream_handler(settings: LogSettings):
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(settings.numeric_level)
    # create formatter
    formatter = logging.Formatter('%(asctime)s: %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add Handeler to logeer 
    logging.getLogger().addHandler(ch)

def _add_file_handler(settings: LogSettings):
    # create file handler and set level to debug
    logfile = REPOSITORY_DIRECTORY.joinpath('logs').joinpath(time.strftime('%Y-%m-%d_%H:%M:%S')+'.log')
    create_paths([logfile]) 
    fh = logging.FileHandler(filename=logfile)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add ch to logger
    logging.getLogger().addHandler(fh)

def setup_handlers(settings: LogSettings):
    """ Add Handlers to Root Loger         
    You can only change console log level by parsing -l or --log
    For the detail, run with option -h 
    """
    logging.getLogger().setLevel(settings.numeric_level)
    _add_stream_handler(settings)
    _add_file_handler(settings)

def setup_root_logger():
    settings = LogSettings(numeric_level=_get_loglevel())
    setup_handlers(settings)
    

if __name__=="__main__":
    setup_root_logger()
    # test 
    logger.critical('Started')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical("critical message")
    logger.critical('Ended')

