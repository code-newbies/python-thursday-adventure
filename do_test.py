from sys import argv
import unittest

help_text = """
Using do_test.py

> python do_test.py     <- run unit tests

> python do_test.py u   <- run unit tests

> python do_test.py f   <- run functional tests

"""

run_unit = False
run_funct = False

if len(argv) == 1:
    run_unit = True
elif len(argv) == 2:
    arg = argv.pop()

    if arg == 'u':
        run_unit = True

    if arg == 'f':
        run_funct = True

if run_unit:
    from tests.items_test import *
    from tests.engine_test import *

if run_funct:
<<<<<<< HEAD
    from tests.functional.inventory_test import *
    from tests.functional.engine_test import *

if run_unit or run_funct:
    if __name__ == '__main__':
#        unittest.main(module=__name__, buffer=True, exit=False)
        unittest.main()
=======
    from functional.inventory_tests import *
    from functional.engine_tests import *

if run_unit or run_funct:
    if __name__ == '__main__':
        unittest.main(warnings='ignore')
>>>>>>> fbe2f51... created do_test.py to run unit and functional tests
else:
    print(help_text)
