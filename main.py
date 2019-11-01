from flask import Flask, request
from classes.soap import Soap
from PydoNovosoft.utils import Utils
from xml.etree import ElementTree
import json_logging
import logging

json_logging.ENABLE_JSON_LOGGING = True
json_logging.init()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

config = Utils.read_config("package.json")

app = Flask(__name__)


def extract_body(xml):
    soap = Soap()
    namespaces = {
        'soap': 'http://www.w3.org/2003/05/soap-envelope'
    }
    node = xml.findall("./soap:Body", namespaces)
    code = 0
    for child in node[0].getchildren():
        data = dict()
        for ele in child.getchildren():
            if "arg0" in ele.tag:
                data["msisdn"] = ele.text
            elif "arg1" in ele.tag:
                data["iccid"] = ele.text
            elif "arg2" in ele.tag:
                data["cveplan"] = ele.text
            elif "arg3" in ele.tag:
                data["cvetpoinst"] = ele.text
        logger.info("New transaction", extra={'props': {"method": child.tag, "app": config["name"],
                                                         "data": data}})
        if child.tag == "alta_aprov_telcel":
            code = soap.alta(data)
    return code


def parse_xml(obj):
    xml = None
    try:
        xml = ElementTree.fromstring(obj)
    except:
        print("Error")
    return xml


@app.route('/', methods=['POST'])
def root():
    logger.info("Request recieved", extra={'props': {"raw": request.data, "app": config["name"],
                                                     "label": config["name"]}})
    code = extract_body(parse_xml(request.data))
    ret = "<?xml version='1.0' encoding='ISO-8859-1' ?><estatus>"+str(code)+"</estatus>"
    logger.info("Response from the service", extra={'props': {"raw": ret, "app": config["name"],
                                                              "label": config["name"], "code": code}})
    return ret


app.run(host='0.0.0.0', port=5000)
