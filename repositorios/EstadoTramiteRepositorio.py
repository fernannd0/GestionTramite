from models.EstadoTramite import EstadoTramite
from models.TipoEstado import TipoEstado
from config.database import conectar
from repositorios.TipoEstadoRepositorio import TipoEstadoRepositorio
from config.database import conectar


class EstadoTramiteRepositorio:

    def buscarEstadoTramite(self, busqueda):  
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        patron=f"%{busqueda}%"
        cursor.execute("""
            SELECT *
            FROM EstadoTramite
            WHERE codEstadoTramite=%s OR nombreEstadoTramite LIKE %s;
        """, (busqueda, patron,))
        r=cursor.fetchall()
        conn.close()
        if isinstance(busqueda, int):
            a=r[0]
            tipoEstado=TipoEstadoRepositorio().buscarTipoEstado(a["codTipoEstado"])
            return EstadoTramite(a["nombreEstadoTramite"], tipoEstado, a["codEstadoTramite"], a["fechaHoraBajaEstadoTramite"])
        resultadoet=[EstadoTramite(a["nombreEstadoTramite"], TipoEstadoRepositorio().buscarTipoEstado(a["codTipoEstado"]), a["codEstadoTramite"], a["fechaHoraBajaEstadoTramite"]) for a in r]
        return resultadoet
    
    def darAltaEstadoTramite(self, et1:EstadoTramite):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            INSERT INTO EstadoTramite (nombreEstadoTramite, codTipoEstado)
            VALUES (%s, %s);

        """, (et1.nombreEstadoTramite, et1.tipoEstado.codTipoEstado))
        conn.commit()
        conn.close()
    
    def traerTodosEstadoTramite(self):
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT *
            FROM EstadoTramite
            ORDER BY fechaHoraBajaEstadoTramite ASC;
        """)
        resultado=cursor.fetchall()
        resultadoet=[EstadoTramite(r["nombreEstadoTramite"], TipoEstadoRepositorio().buscarTipoEstado(r["codTipoEstado"]), r["codEstadoTramite"], r["fechaHoraBajaEstadoTramite"]) for r in resultado]
        conn.close()
        return resultadoet

    def actualizarEstadoTramite(self, et1:EstadoTramite):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE EstadoTramite
            SET nombreEstadoTramite=%s,
                codTipoEstado=%s
            WHERE codEstadoTramite=%s;
        """, (et1.nombreEstadoTramite, et1.tipoEstado.codTipoEstado, et1.codEstadoTramite))
        conn.commit()
        conn.close()

    def darBajaEstadoTramite(self, et1:EstadoTramite):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE EstadoTramite
            SET fechaHoraBajaEstadoTramite=%s
            WHERE codEstadoTramite=%s;
        """, (et1.fechaHoraBajaEstadoTramite, et1.codEstadoTramite))
        conn.commit()
        conn.close()