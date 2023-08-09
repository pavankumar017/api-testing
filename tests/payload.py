import mysql.connector

def get_payload():
    payload = {
        "name": "Learn Appium Automation with Java",
        "isbn": "bcdadf",
        "aisle": "227",
        "author": "John foe"
    }
    return payload


def build_payload_fromDB():
    addBody = {}
    db_resp = get_query()
    print(db_resp)   
    addBody['name'] = db_resp[0]
    addBody['isbn'] = db_resp[1]
    addBody['aisle'] = db_resp[2]
    addBody['author'] = db_resp[3]
    return addBody


def get_query():
    conn = mysql.connector.connect(host = 'localhost' , database= 'PythonAutomation', user = 'root', password = 'root1234')
    print(conn.is_connected())
    cur = conn.cursor()
    cur.execute('use APIDevelop')
    cur.execute('select * from Books')
    row = cur.fetchone()
    print(row)
    return row