import subprocess

USAGE = "poc-y [options]"

VERSION = "1.0"
BANNER = """
__________________  _________          _____.___.
\______   \_____  \ \_   ___ \         \__  |   |
 |     ___//   |   \/    \  \/   ______ /   |   |
 |    |   /    |    \     \____ /_____/ \____   |
 |____|   \_______  /\______  /         / ______|
                  \/        \/          \/
                  author@Recar   version {}
""".format(VERSION)

POC_DIR="/pocs"

IS_WIN = subprocess._mswindows
UNICODE_ENCODING = "utf-8"