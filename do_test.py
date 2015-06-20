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
<<<<<<< HEAD
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
=======
    from functional.inventory_test import *
    from functional.engine_test import *
=======
    from tests.functional.inventory_test import *
    from tests.functional.engine_test import *
>>>>>>> 376ef97... Creates main loop and allows 'Q' to exit the main loop

if run_unit or run_funct:
    if __name__ == '__main__':
<<<<<<< HEAD
        unittest.main(module=__name__, buffer=True, exit=False)
>>>>>>> 4a69152... created fucntional test that allows stdout to be read and allows input to be passed to the program
=======
#        unittest.main(module=__name__, buffer=True, exit=False)
        unittest.main()
>>>>>>> 579a2d6... Updated to use passed in output function rather than print. This will make for cleaner tests.
else:
    print(help_text)
