from unittest import TestCase
from classes.soap import Soap


class TestAprovisionamiento(TestCase):

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

    def test_iccd(self):
        params = dict()
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 200)

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
        self.assertTrue(js == 401)

    def test_existente(self):
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 501)

    def test_vacios(self):
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 600)

    def test_asociado(self):
        params["msisdn"] = ""
        params["iccid"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 900)
