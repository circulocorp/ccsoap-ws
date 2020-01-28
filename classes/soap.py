from classes.database import Database
from PydoNovosoft.utils import Utils
import json_logging
import logging
import sys

json_logging.ENABLE_JSON_LOGGING = True
json_logging.init()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))
config = Utils.read_config("package.json")


class Soap(object):

    def validate(self, params):
        if "msisdn" not in params or len(params["msisdn"]) != 12:
            logger.info("MSSID is not equals to 12", extra={'props': {"raw": params, "app": config["name"], "label": config["name"]}})
            return 100
        if "msisdn" in params:
            try:
                int(params["msisdn"])
            except:
                logger.error("MSSID is not numeric", extra={'props': {"raw": params, "app": config["name"], "label": config["name"]}})
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
        logger.info("Request COM_6 processing", extra={'props': {"raw": params, "app": config["name"], "label": config["name"]}})
        code = self.validate(params)
        if code == 0:
            db = Database(dbhost=Utils.get_secret("pg_host"), dbuser=Utils.get_secret("soapdbuser"),
                          dbpass=Utils.get_secret("soapdbpass"))
            rows = db.find_msisdn(params["msisdn"])
            logger.info("Finding rows:"+str(len(rows)), extra={'props': {"raw": params, "app": config["name"], "label": config["name"]}})
            if len(rows) < 1:
                code = 406
            else:
                value = rows[0]
                code = value["msisdn"]+"|"+value["iccid"]+"|"+value["cveplan"]+"|"+value["cvetpoinst"]+"|"+value["estado"]
                if value["estado"] == "SUSPENDIDA":
                    code = code + "|"+str(700)
                elif value["estado"] == "CANCELAR":
                    code = code + "|" + str(800)
        return code
