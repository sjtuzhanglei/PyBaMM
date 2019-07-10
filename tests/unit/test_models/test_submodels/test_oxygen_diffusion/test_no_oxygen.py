#
# Test constant concentration submodel
#

import pybamm
import tests
import unittest


class TestConstantConcentration(unittest.TestCase):
    def test_public_functions(self):
        param = pybamm.standard_parameters_lead_acid
        submodel = pybamm.oxygen_diffusion.NoOxygen(param)
        std_tests = tests.StandardSubModelTests(submodel)
        std_tests.test_all()


if __name__ == "__main__":
    print("Add -v for more debug output")
    import sys

    if "-v" in sys.argv:
        debug = True
    pybamm.setting.debug_mode = True
    unittest.main()
