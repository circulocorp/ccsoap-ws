from unittest import TestCase
from classes.soap import Soap


class TestSuspension(TestCase):

    def test_exitosa(self):
        params = dict()
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 0)

    def test_mssid(self):
        params = dict()
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 100)


    def test_formato(self):
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 300)

    def test_noexistoso(self):
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 402)

    def test_suspendido(self):
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 502)

