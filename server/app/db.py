import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            charset="utf8mb4",
            connect_timeout=31536000,
            cursorclass=pymysql.cursors.DictCursor,
            db="freedb_homiracle",
            host='sql.freedb.tech',
            password='rc%kc*n8N28MYgk',
            read_timeout=100000,
            port=3306,
            user='freedb_Homiracle_admin',
            write_timeout=100000,   
        )

    def get_cursor(self):
        return self.connection.cursor()