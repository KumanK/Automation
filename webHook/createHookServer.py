from flask import Flask, request, Response
import time
import sys

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json)
    print("Executing acceptance suite")
    return Response(status=200)


if __name__ == '__main__':
    app.run()