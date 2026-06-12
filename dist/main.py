from flask import Flask, request, send_from_directory, jsonify
import pymysql

app = Flask(__name__)

# db = pymysql.connect(
#     host='mysql', 
#     port=3306,
#     user='root',
#     password='1234',
#     database='mydb',
#     charset='utf8'
# )

@app.route('/')
def home():
    return send_from_directory('./dist','index.html')

@app.route('/<path:path>')
def serve_react(path):
    return send_from_directory;

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=3300, debug=True, use_reloader=False)
