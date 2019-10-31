from flask import Flask, request
from classes.soap import Soap
from xml.etree import ElementTree

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
        code = soap.validate(data)
        if child.tag == "alta_aprov_telcel" and code == 1:
            code = alta(data)
    return code


def parse_xml(obj):
    xml = None
    try:
        xml = ElementTree.fromstring(obj)
    except:
        print("Error")
    return xml


def alta(data):
    print(data)
    return 200


@app.route('/', methods=['POST'])
def root():
    code = extract_body(parse_xml(request.data))
    ret = "<?xml version='1.0' encoding='ISO-8859-1' ?><estatus>"+str(code)+"</estatus>"
    return ret


app.run(host='0.0.0.0', port=5000)
