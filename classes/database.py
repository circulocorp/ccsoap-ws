import psycopg2 as pg


class Database(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._conn = None

    def _connect(self):
        try:
            conn = pg.connect(host=self.dbhost, user=self.dbuser, password=self.dbpass, port="5432",
                              database="telcelgvt")
            self._conn = conn
        except (Exception, pg.Error) as error:
            print(error)

    def find_mssid(self, mssid):
        sql = "select * from 'APRVD_TELCEL_TRANS' where 'APRV_D_MSISDN' = %s"
        recs = []
        if not self._conn:
            self._connect()
        try:
            cursor = self._conn.cursor()
            cursor.execute(sql, (mssid))
            data = cursor.fetchall()
            for row in data:
                rec = {}
                rec["telcel"] = row[0]
                rec["key"] = row[1]
                rec["mssid"] = row[2]
                rec["iccid"] = row[3]
                rec["cveplan"] = row[4]
                rec["cvetpoinst"] = row[5]
                rec["created"] = row[6]
                rec["cveplannew"] = row[7]
                rec["estado"] = row[8]
                recs.append(rec)
        except (Exception, pg.Error) as error:
            print(error)
        finally:
            return recs

    def insert_telcel_trans(self, values):
        sql = "insert into 'APRVD_TELCEL_TRANS'('APRV_C_TELCEL','APRV_D_KEY','APRV_D_MSISDN','APRV_D_ICCID'," \
              "'APRV_D_CVEPLAN','APRV_D_CVETPOINST','DATE_CREATED','APRV_D_CVEPLAN_NEW','APRV_B_ESTADO') values(" \
              "%s,%s,%s,%s,%s,%s,NOW(),%s,%s)"
        if not self._conn:
            self._connect()
        cursor = self._conn.cursor()
        cursor.execute(sql, (values["telcel"], values["key"], values["mssid"], values["iccid"], values["cveplan"],
                             values["cvetpoinst"], values["cveplannew"], values["estado"]))
        self._conn.commit()

    def update_telcel_trans(self, values):
        sql = "update 'APRVD_TELCEL_TRANS' set 'APRV_C_TELCEL'=%s,'APRV_D_KEY'=%s,'APRV_D_ICCID'=%s," \
              "'APRV_D_CVEPLAN'=%s,'APRV_D_CVETPOINST'=%s,'APRV_D_CVEPLAN_NEW'=%s,'APRV_B_ESTADO'=%s " \
              "where 'APRV_D_MSISDN'=%s"
        if not self._conn:
            self._connect()
        cursor = self._conn.cursor()
        cursor.execute(sql, (values["telcel"], values["key"], values["iccid"], values["cveplan"],
                             values["cvetpoinst"], values["cveplannew"], values["estado"], values["mssid"]))
        self._conn.commit()
