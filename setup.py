# cxfreeze version, but that leaves too many files

from cx_Freeze import setup, Executable
import sys


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "goongradecalc",
      version = "4",
      description = "",
      executables = [Executable("main.pyw", base=base)])

