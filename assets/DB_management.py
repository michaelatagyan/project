import os, sqlite3, sys


def Path():
    if getattr(sys, 'frozen', False):
        path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(sys.argv[0])))
        return path
    else:
        path = os.path.dirname(os.path.abspath(sys.argv[0]))
        return path


class DB_management():
    def __init__(self):
        self.database_path = os.path.join(Path(), 'assets', 'identifier.db3')

    def exec(self, query, params=None):
        self.con = sqlite3.connect(self.database_path)
        self.cur = self.con.cursor()
        if params:
            r = self.cur.execute(f'{query}', (params,))
        else:
            r = self.cur.execute(f'{query}')
        data = r.fetchall()
        self.con.close()
        return data

DB = DB_management()

