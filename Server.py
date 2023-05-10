from flask import Flask, jsonify, request
from Data_Masker import check_database_connection
app = Flask(__name__)

@app.route('/Data_mask', methods=['POST'])
def Check_Connection():
    host=request.form['host']
    database = request.form['database']
    user = request.form['user']
    password = request.form['password']
    port = request.form['port']
    print(host + database + user + password + port)
    is_successful = check_database_connection(host, database, user, password, port)
    if is_successful:
        print("Database connection successful!")
    else:
        print("Unable to connect to the database. Kindly Check the Connection Details/VPN.")
    response = {'success': is_successful}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
