

class Soap(object):

    def alta(self, params):
        code = 0
        if "MSISDN" not in params or len(params["MSISDN"]) < 12:
            code = 100
        if "ICCID" not in params or len(params["ICCID"]) < 19:
            code = 200
        if "ICCID" in params and "MSISDN" in params:
            if not isinstance(params["ICCID"], int) and not isinstance(params["MSISDN"], int):
                code = 300
        return code

    def suspension(self, params):
        code = 0
        if "MSISDN" not in params or len(params["MSISDN"]) < 12:
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

