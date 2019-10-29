from classes.database import Database
from PydoNovosoft.utils import Utils

class Soap(object):

    def validate(self, params):
        if "msisdn" not in params or len(params["msisdn"]) < 12:
            return 100
        if "iccid" not in params or len(params["iccid"]) < 19:
            return 200
        if "msisdn" in params:
            if not isinstance(params["msisdn"], int):
                return 300
        return 1

    def alta(self, params):
        code = self.validate(params)
        if code == 1:
            db = Database(dbhost=Utils.get_secret("pghost"), dbuser=Utils.get_secret("soapdbuser"),
                          dbpass=Utils.get_secret("soapdbpass"))
            rows = db.find_iccid(params["iccid"])
            if len(rows) > 0:
                code = 600
            else:
                db.insert_telcel_trans(params)
        return code

    def suspension(self, params):
        code = 0
        if "msisdn" not in params or len(params["msisdn"]) < 12:
            code = 100
        if "MSISDN" in params:
            if not isinstance(params["MSISDN"], int):
                code = 300
        return code

    def reactivacion(self, params):
        code = 0
        if "MSISDN" not in params or len(params["MSISDN"]) < 12:
            code = 100
        if "MSISDN" in params:
            if not isinstance(params["MSISDN"], int):
                code = 300
        return code

    def cancelacion(self, params):
        code = 0
        if "MSISDN" not in params or len(params["MSISDN"]) < 12:
            code = 100
        if "MSISDN" in params:
            if not isinstance(params["MSISDN"], int):
                code = 300
        return code

    def update_plan(self, params):
        code = 0
        if "MSISDN" not in params or len(params["MSISDN"]) < 12:
            code = 100
        if "MSISDN" in params:
            if not isinstance(params["MSISDN"], int):
                code = 300
        return code

