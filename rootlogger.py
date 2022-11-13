import argparse
import logging
import time
import sys

logger = logging.getLogger(__name__)

def _get_loglevel() -> :
    """ get loglevel from command line argment
    Return:
        numeric_level(int):Number assined to each logging level 
                           See https://docs.python.org/ja/3/library/logging.html?highlight=logging%20debug
        
    """
    parser = argparse.ArgumentParser()
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

def setup_root_logger():
    """ Setup root logger         
    You can only change console log level by parsing -l or --log
    For the detail, run with option -h 
    """
    logger = logging.getLogger()
    numeric_level=_get_loglevel()
    logger.setLevel(numeric_level)
    
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(numeric_level)
    # create formatter
    formatter = logging.Formatter('%(asctime)s: %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)
    # add Handeler to logeer 
    logger.addHandler(ch)

    # create file handler and set level to debug
    logfile = "./log/" + time.strftime('%Y-%m-%d_%H:%M:%S') + '.log'
    fh = logging.FileHandler(filename=logfile)
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(fh)

if __name__=="__main__":
    setup_root_logger()
    logger.critical('Started')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical("critical message")
    logger.criical('Ended')

