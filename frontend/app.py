from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="db",
    user="root",
    password="root",
    database="multi-container-app"
)

@app.route('/')
def home():
    return "Welcome to the Multi-Container App"

@app.route('/get_vaccination_status', methods=['POST'])
def get_vaccination_status():
    reg_no = request.form.get('reg_no')
    cursor = db.cursor()
    cursor.execute("SELECT Vaccination_Status FROM Students WHERE RegNo=%s", (reg_no,))
    result = cursor.fetchone()
    if result:
        return jsonify({"status": result[0]})
    else:
        return jsonify({"status": "No data found"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
