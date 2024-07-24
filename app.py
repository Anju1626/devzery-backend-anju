from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

# Database connection parameters
DB_NAME = "devzery_database"
DB_USER = "tester"
DB_PASSWORD = "test_password"
DB_HOST = "localhost"  # Usually "localhost" if on the same machine
DB_PORT = "5432"  # Default PostgreSQL port

def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

@app.route('/api/testcases', methods=['GET'])
def get_test_cases():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM testcases")
    test_cases = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(test_cases)

@app.route('/api/testcases/<int:case_id>', methods=['PUT'])
def update_test_case(case_id):
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "UPDATE testcases SET status = %s WHERE id = %s RETURNING *",
        (data['status'], case_id)
    )
    updated_case = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if updated_case:
        return jsonify(updated_case), 200
    return jsonify({"error": "Test case not found"}), 404

@app.route('/api/testcases/search', methods=['GET'])
def search_test_cases():
    query = request.args.get('query', '').lower()
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(
        "SELECT * FROM testcases WHERE LOWER(name) LIKE %s OR LOWER(module) LIKE %s",
        (f'%{query}%', f'%{query}%')
    )
    filtered_cases = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(filtered_cases)

if __name__ == '__main__':
    app.run(debug=True, port=3001)