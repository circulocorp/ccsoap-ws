from tests.test_aprovision import TestAprovisionamiento
from tests.test_cancelacion import TestCancelacion
from tests.test_modificacion import TestModificacion
from tests.test_reactivacion import TestReactivacion
from tests.test_suspension import TestSuspension
from unittest import TestCase, TestSuite, TestResult


class TestAll(TestCase):

    def suite(self):
        print("Tests")


if __name__ == "__main__":
    unittest.main()
