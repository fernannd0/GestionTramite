from config.database import conectar
from models.TipoEstado import TipoEstado

class TipoEstadoRepositorio:

    def traerTodosTipoEstado(self):
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT *
            FROM TipoEstado;
        """)
        resultado=cursor.fetchall()
        conn.close()
        return [TipoEstado(r["nombreTipoEstado"], r["codTipoEstado"]) for r in resultado]

    def buscarTipoEstado(self, cod):
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT *
            FROM TipoEstado
            WHERE codTipoEstado = %s;
        """, (cod,))
        resultado=cursor.fetchone()
        conn.close()
        return TipoEstado(resultado["nombreTipoEstado"], resultado["codTipoEstado"])