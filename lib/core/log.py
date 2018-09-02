import logging
import sys,os
import ctypes
from lib.core.enums import CUSTOM_LOGGING


FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN

STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool


logging.addLevelName(CUSTOM_LOGGING.SYSINFO, "*")
logging.addLevelName(CUSTOM_LOGGING.SUCCESS, "+")
logging.addLevelName(CUSTOM_LOGGING.ERROR, "-")
logging.addLevelName(CUSTOM_LOGGING.WARNING, "!")

LOGGER = logging.getLogger("poc-y")

LOGGER_HANDLER = None
try:
    from thirdparty.ansistrm.ansistrm import ColorizingStreamHandler

    try:
        LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)
        LOGGER_HANDLER.level_map[logging.getLevelName("*")] = (None, "cyan", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("+")] = (None, "green", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("-")] = (None, "red", False)
        LOGGER_HANDLER.level_map[logging.getLevelName("!")] = (None, "yellow", False)
    except Exception as e:
        print(e)
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

except ImportError as e:
    print(e)
    LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

FORMATTER = logging.Formatter("\r[%(asctime)s] [%(levelname)s] %(message)s", "%H:%M:%S")

LOGGER_HANDLER.setFormatter(FORMATTER)
LOGGER.addHandler(LOGGER_HANDLER)
LOGGER.setLevel(CUSTOM_LOGGING.WARNING)


class MY_LOGGER:
    @staticmethod
    def success(msg):
        set_color(FOREGROUND_GREEN)
        LOGGER.log(CUSTOM_LOGGING.SUCCESS, msg)
        set_color(FOREGROUND_WHITE)

    @staticmethod
    def info(msg):
        LOGGER.log(CUSTOM_LOGGING.SYSINFO, msg)

    @staticmethod
    def warning(msg):
        set_color(FOREGROUND_YELLOW)
        LOGGER.log(CUSTOM_LOGGING.WARNING, msg)
        set_color(FOREGROUND_WHITE)

    @staticmethod
    def error(msg):
        set_color(FOREGROUND_RED)
        LOGGER.log(CUSTOM_LOGGING.ERROR, msg)
        set_color(FOREGROUND_WHITE)
