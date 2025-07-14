"""
    Config file contains all project constants
"""

from platform import platform


BPS = 9600

# Check name on your computer
PORTNAME = '/dev/serial0' if '-rpi-' in platform() else "COM7"


PACKAGE_SIZE = 66
RESERVED_BYTES = 2
USEFUL_PACKAGE_SIZE = PACKAGE_SIZE - RESERVED_BYTES
