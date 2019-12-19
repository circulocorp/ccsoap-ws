from unittest import TestCase
from classes.soap import Soap


class TestAprovisionamiento(TestCase):

    def test_exitosa(self):
        params = dict()
        params["msisdn"] = "525546868951"
        params["iccid"] = "019912311111112223"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 0)

    def test_mssid(self):
        params = dict()
        params["msisdn"] = "46868951"
        params["iccid"] = "0199123111111122233"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 100)

    def test_iccd(self):
        params = dict()
        params["msisdn"] = "525546868951"
        params["iccid"] = "0199123111111122231123232"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 200)

    def test_formato(self):
        params = dict()
        params["msisdn"] = "asdsadsasdsa"
        params["iccid"] = "0199123111111122231"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 300)

    def test_noexistoso(self):
        params = dict()
        params["msisdn"] = "525546868951"
        params["iccid"] = "019912311111112223"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 401)

    def test_existente(self):
        params = dict()
        params["msisdn"] = "525546868951"
        params["iccid"] = "0199123111111122231"
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 501)

    def test_vacios(self):
        params = dict()
        params["msisdn"] = "525546868951"
        params["iccid"] = "0199123111111122231"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 600)

    def test_asociado(self):
        params = dict()
        params["msisdn"] = "525546868952"
        params["iccid"] = "0199123111111122231"
        params["cveplan"] = ""
        params["cvetpoinst"] = ""
        soap = Soap()
        js = soap.alta(params)
        self.assertTrue(js == 900)
