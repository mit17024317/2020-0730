#!/usr/bin/env python3
"""stop watch """

__author__ = "R.Nakata"
__date__ = "2020/02/07"
import time
from functools import wraps
from logging import getLogger

logger = getLogger(__name__)


def stop_watch(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        start = time.time()
        result = func(*args, **kargs)
        elapsed_time = time.time() - start
        logger.debug(f"{func.__name__} took {elapsed_time}")
        return result

    return wrapper
