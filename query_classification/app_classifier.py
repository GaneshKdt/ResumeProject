from flask import Flask, request
import sys
sys.path.append(r"C:\Users\Ganesh\Documents\Resume Project\query_classification\query_classification")
from classifier import result


app = Flask(__name__)

@app.route('/result/<string:query>', methods=['GET'])
def get_result(query):
    #return result
    return result(query)
if __name__ == '__main__':
    app.run()

#http://127.0.0.1:5000/result/
