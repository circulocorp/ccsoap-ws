from unittest import TestCase
from classes.soap import Soap


class TestCancelacion(TestCase):

    def test_exitosa(self):
        params = dict()
        params["msisdn"] = "525546868951"
        params["iccid"] = "019912311111112223"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.cancelacion(params)
        self.assertTrue(js == 0)

    def test_mssid(self):
        params = dict()
        params["msisdn"] = "46868951"
        params["iccid"] = "019912311111112223"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.cancelacion(params)
        self.assertTrue(js == 100)

    def test_formato(self):
        params = dict()
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.cancelacion(params)
        self.assertTrue(js == 300)

    def test_noexiste(self):
        params = dict()
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.cancelacion(params)
        self.assertTrue(js == 404)

    def test_cancelado(self):
        params = dict()
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.cancelacion(params)
        self.assertTrue(js == 504)
