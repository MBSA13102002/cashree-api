import requests as rm
import json
from flask import Flask,request
from flask_cors import CORS
cors = CORS(app)
headers_dict = {
    "x-client-id": "78975f8bd06ac31b2981a9e1d57987",
    "x-client-secret": "3e2d92a5a03af93ddb1396af73388cf6df51f102"
    }

app = Flask(__name__)



@app.route("/cashfree/<string:orderId>/<string:orderAmount>",methods = ['GET','POST'])
def start(orderId,orderAmount):
        data ={
            "orderId": orderId,
            "orderAmount":int(orderAmount),
            "orderCurrency": "INR"}
        response = rm.post(url = "https://test.cashfree.com/api/v2/cftoken/order",json = data, headers=headers_dict)
        return json.loads(response.text)['cftoken']


