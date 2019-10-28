from flask import Flask, request
from classes.soap import Soap
from xml.etree import ElementTree

app = Flask(__name__)


def extract_body(xml):
    namespaces = {
        'soap': 'http://www.w3.org/2003/05/soap-envelope'
    }
    node = xml.findall("./soap:Body", namespaces)
    print(node)
    return dict()


def parse_xml(obj):
    xml = None
    try:
        xml = ElementTree.fromstring(obj)
    except e:
        print("Error")
    return xml


@app.route('/alta', methods=['POST'])
def alta():
    soap = Soap()
    data = extract_body(parse_xml(request.data))
    print(xml.getchildren())
    code = soap.alta(dict())
    ret = "<?xml version='1.0' encoding='ISO-8859-1' ?><estatus>"+str(code)+"</estatus>"
    return ret


app.run(host='0.0.0.0', port=5000)
