from classes.database import Database
from PydoNovosoft.utils import Utils


class Soap(object):

    def validate(self, params):
        if "msisdn" not in params or len(params["msisdn"]) != 12:
            return 100
        if "msisdn" in params:
            try:
                int(params["msisdn"])
            except:
                return 300
        return 0

    def alta(self, params):
        code = self.validate(params)
        if code == 0:
            if "iccid" not in params or len(params["iccid"]) != 19:
                code = 200
            elif "cveplan" not in params or params["cveplan"] == "":
                code = 600
            elif "cvetpoinst" not in params or params["cvetpoinst"] == "":
                code = 600
            else:
                db = Database(dbhost=Utils.get_secret("pg_host"), dbuser=Utils.get_secret("soapdbuser"),
                              dbpass=Utils.get_secret("soapdbpass"))
                rows = db.find_iccid(params["iccid"])
                if len(rows) > 0:
                    code = 501
                else:
                    id = db.insert_telcel_trans(params)
                    if int(id) > 0:
                        rec = db.select_telcel(id)
                        code = db.insert_telcel_hist(rec)
                    else:
                        code = 401
        return code

    def suspension(self, params):
        code = self.validate(params)
        if code == 0:
            db = Database(dbhost=Utils.get_secret("pg_host"), dbuser=Utils.get_secret("soapdbuser"),
                          dbpass=Utils.get_secret("soapdbpass"))
            rows = db.find_msisdn(params["msisdn"])
            if len(rows) < 1:
                code = 502
            else:
                values = rows[0]
                if values["estado"] != "ALTA":
                    code = 502
                else:
                    values["estado"] = "SUSPENSION"
                    code = db.update_telcel_trans(values)
                    db.insert_telcel_hist(values)
        return code

    def reactivacion(self, params):
        code = self.validate(params)
        if code == 0:
            db = Database(dbhost=Utils.get_secret("pg_host"), dbuser=Utils.get_secret("soapdbuser"),
                          dbpass=Utils.get_secret("soapdbpass"))
            rows = db.find_msisdn(params["msisdn"])
            if len(rows) < 1:
                code = 503
            else:
                values = rows[0]
                if values["estado"] != "SUSPENSION":
                    code = 503
                else:
                    values["estado"] = "ALTA"
                    code = db.update_telcel_trans(values)
                    db.insert_telcel_hist(values)
        return code

    def cancelacion(self, params):
        code = self.validate(params)
        if code == 0:
            db = Database(dbhost=Utils.get_secret("pg_host"), dbuser=Utils.get_secret("soapdbuser"),
                          dbpass=Utils.get_secret("soapdbpass"))
            rows = db.find_msisdn(params["msisdn"])
            if len(rows) < 1:
                code = 503
            else:
                values = rows[0]
                if values["estado"] != "ALTA":
                    code = 503
                else:
                    values["estado"] = "CANCELAR"
                    code = db.update_telcel_trans(values)
                    db.insert_telcel_hist(values)
        return code

    def update_plan(self, params):
        code = self.validate(params)
        if code == 0:
            db = Database(dbhost=Utils.get_secret("pg_host"), dbuser=Utils.get_secret("soapdbuser"),
                          dbpass=Utils.get_secret("soapdbpass"))
            rows = db.find_msisdn(params["msisdn"])
            if len(rows) < 1:
                code = 700
            else:
                values = rows[0]
                if values["estado"] != "ALTA":
                    code = 700
                else:
                    values["cveplannew"] = params["cveplannew"]
                    code = db.update_telcel_trans(values)
                    db.insert_telcel_hist(values)
        return code

    def com_6(self, params):
        code = self.validate(params)
        if code == 0:
            db = Database(dbhost=Utils.get_secret("pg_host"), dbuser=Utils.get_secret("soapdbuser"),
                          dbpass=Utils.get_secret("soapdbpass"))
            rows = db.find_msisdn(params["msisdn"])
            if len(rows) < 1:
                code = 405
            else:
                value = rows[0]
                code = value["msisdn"]+"|"+value["iccid"]+"|"+value["cveplan"]+"|"+value["cvetpoinst"]+"|"+value["estado"]
                if value["estado"] == "SUSPENDIDA":
                    code = code + "|"+str(700)
                elif value["estado"] == "CANCELAR":
                    code = code + "|" + str(800)
        return code
