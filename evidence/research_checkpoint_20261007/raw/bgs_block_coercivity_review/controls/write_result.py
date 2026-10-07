#!/usr/bin/env python3
import contextlib, runpy, sys
with open(sys.argv[2], 'w', encoding='utf-8') as result:
    with contextlib.redirect_stdout(result):
        runpy.run_path(sys.argv[1], run_name='__main__')
