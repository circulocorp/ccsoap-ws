import psycopg2 as pg


class Database(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self._conn = None
        self._connect()

    def _connect(self):
        try:
            conn = pg.connect(host=self.dbhost, user=self.dbuser, password=self.dbpass, port="5432",
                              database="telcelgvt")
            self._conn = conn
        except (Exception, pg.Error) as error:
            print(error)
            self._conn = None

    def select_telcel(self, id):
        sql = "select * from 'APRVD_TELCEL_TRANS' where 'APRV_C_TELCEL' = %s"
        recs = []
        if not self._conn:
            self._connect()
        try:
            cursor = self._conn.cursor()
            cursor.execute(sql, (msisdn, ))
            data = cursor.fetchall()
            for row in data:
                rec = {}
                rec["telcel"] = row[0]
                rec["key"] = row[1]
                rec["msisdn"] = row[2]
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

    def find_msisdn(self, msisdn):
        sql = "select * from 'APRVD_TELCEL_TRANS' where 'APRV_D_MSISDN' = %s"
        recs = []
        if not self._conn:
            self._connect()
        try:
            cursor = self._conn.cursor()
            cursor.execute(sql, (msisdn, ))
            data = cursor.fetchall()
            for row in data:
                rec = {}
                rec["telcel"] = row[0]
                rec["key"] = row[1]
                rec["msisdn"] = row[2]
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

    def find_iccid(self, iccid):
        sql = "select * from 'APRVD_TELCEL_TRANS' where 'APRV_D_ICCID' = %s"
        recs = []
        if not self._conn:
            self._connect()
        try:
            cursor = self._conn.cursor()
            cursor.execute(sql, (msisdn, ))
            data = cursor.fetchall()
            for row in data:
                rec = {}
                rec["telcel"] = row[0]
                rec["key"] = row[1]
                rec["msisdn"] = row[2]
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
        try:
            sql = "insert into 'APRVD_TELCEL_TRANS'('APRV_D_KEY','APRV_D_MSISDN','APRV_D_ICCID'," \
                  "'APRV_D_CVEPLAN','APRV_D_CVETPOINST','DATE_CREATED','APRV_D_CVEPLAN_NEW','APRV_B_ESTADO') values(" \
                  "'3c06b14346f35e59f63d7fce97340220d77b9ac2',%s,%s,%s,%s,NOW(),NULL,'ALTA') RETURNING 'APRV_C_TELCEL'"
            if not self._conn:
                self._connect()
            cursor = self._conn.cursor()
            print(sql)
            cursor.execute(sql, (values["msisdn"], values["iccid"], values["cveplan"], values["cvetpoinst"], ))
            id = cursor.fetchone()[0]
            self._conn.commit()
            cursor.close()
            return id
        except (Exception, pg.Error) as error:
            print(error)
            return 0

    def insert_telcel_hist(self, values):
        try:
            sql = "insert into 'APRVH_TELCEL_HIST'('APRV_C_TELCEL','APRV_D_KEY','APRV_D_MSISDN','APRV_D_ICCID'," \
                  "'APRV_D_CVEPLAN','APRV_D_CVETPOINST','DATE_CREATED','APRV_D_CVEPLAN_NEW','APRV_B_ESTADO', " \
                  "'DATE_CREATED_INSERTADO') values(%s,'3c06b14346f35e59f63d7fce97340220d77b9ac2',%s,%s,%s,%s,NOW()," \
                  "%s,%s, %s)"
            if not self._conn:
                self._connect()
            cursor = self._conn.cursor()
            cursor.execute(sql, (values["telcel"], values["msisdn"], values["iccid"], values["cveplan"],
                                 values["cvetpoinst"], values["cveplannew"], values["estado"], values["created"], ))
            self._conn.commit()
            cursor.close()
            return 0
        except (Exception, pg.Error) as error:
            print(error)
            return 501

    def update_telcel_trans(self, values):
        sql = "update 'APRVD_TELCEL_TRANS' set 'APRV_C_TELCEL'=%s,'APRV_D_KEY'=%s,'APRV_D_ICCID'=%s," \
              "'APRV_D_CVEPLAN'=%s,'APRV_D_CVETPOINST'=%s,'APRV_D_CVEPLAN_NEW'=%s,'APRV_B_ESTADO'=%s " \
              "where 'APRV_D_MSISDN'=%s"
        if not self._conn:
            self._connect()
        cursor = self._conn.cursor()
        cursor.execute(sql, (values["telcel"], values["key"], values["iccid"], values["cveplan"],
                             values["cvetpoinst"], values["cveplannew"], values["estado"], values["msisdn"]))
        self._conn.commit()
