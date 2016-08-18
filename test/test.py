from win32 import path
path.add_parent(__file__, levels=1)

from sru.main import run

run()
