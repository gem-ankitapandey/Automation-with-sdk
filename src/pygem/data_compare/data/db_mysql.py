import traceback
import pymysql

class Database():

    def __init__(self,config_data) -> None:
        self.user = config_data.get("user",None)
        self.host = config_data.get("host", None)
        self.port = config_data.get("port", None)
        if isinstance(self.port,str):
            self.port = int(self.port)
        self.password = config_data.get("password", None)
        self.database = config_data.get("databse", None)
        
    def connect(self):
        try:
            self.con = pymysql.connect(host = self.host, user = self.user, password = self.password, port = self.port,database = self.database)
            print("Connected successfully")
            self.cursor = self.con.cursor()
            print("Cursor created")
        except Exception:
            print("Exception in connect {}".format(traceback.format_exc()))

    def execute_query(self, query, header = False):
        try:
            self.cursor.execute(query)
            res = self.cursor.fetchall()
            if header:
                q_header = [x[0] for x in self.cursor.description]
            else:
                q_header = []
        except Exception:
            print("Exception in execute_query {}".format(traceback.format_exc()))
        return res,q_header if header else res

    def close(self):
        try:
            self.con.close()
        except Exception:
            print("Exception in cose {}".format(traceback.format_exc()))