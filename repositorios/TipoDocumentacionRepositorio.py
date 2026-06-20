from models.TipoDocumentacion import TipoDocumentacion
from config.database import conectar

class TipoDocumentacionRepositorio:

    def buscarTipoDocumentacion(self, busqueda):  
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        patron=f"%{busqueda}%"
        cursor.execute("""
            SELECT *
            FROM TipoDocumentacion
            WHERE codTipoDocumentacion=%s OR nombreTipoDocumentacion LIKE %s;
        """, (busqueda, patron,))
        r=cursor.fetchall()
        conn.close()
        if isinstance(busqueda, int):
            a=r[0]
            return TipoDocumentacion(a["nombreTipoDocumentacion"], a["requiereEntregaWeb"], a["codTipoDocumentacion"], a["fechaHoraBajaTipoDocumentacion"])
        resultadotd=[TipoDocumentacion(res["nombreTipoDocumentacion"], res["requiereEntregaWeb"], res["codTipoDocumentacion"], res["fechaHoraBajaTipoDocumentacion"])for res in r]
        return resultadotd
    
    def darAltaTipoDocumentacion(self, t1:TipoDocumentacion):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            INSERT INTO TipoDocumentacion (nombreTipoDocumentacion, requiereEntregaWeb)
            VALUES (%s, %s);

        """, (t1.nombreTipoDocumentacion, t1.requiereEntregaWeb))
        conn.commit()
        conn.close()
    
    def traerTodosTipoDocumentacion(self):
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT *
            FROM TipoDocumentacion
            ORDER BY fechaHoraBajaTipoDocumentacion ASC;
        """)
        resultado=cursor.fetchall()
        resultadotd=[TipoDocumentacion(r["nombreTipoDocumentacion"], r["requiereEntregaWeb"], r["codTipoDocumentacion"], r["fechaHoraBajaTipoDocumentacion"]) for r in resultado]
        conn.close()
        return resultadotd

    def actualizarTipoDocumentacion(self, t1:TipoDocumentacion):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE TipoDocumentacion
            SET nombreTipoDocumentacion=%s,
                requiereEntregaWeb=%s
            WHERE codTipoDocumentacion=%s;
        """, (t1.nombreTipoDocumentacion, t1.requiereEntregaWeb, t1.codTipoDocumentacion))
        conn.commit()
        conn.close()

    def darBajaTipoDocumentacion(self, t1:TipoDocumentacion):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE TipoDocumentacion
            SET fechaHoraBajaTipoDocumentacion=%s
            WHERE codTipoDocumentacion=%s;
        """, (t1.fechaHoraBajaTipoDocumentacion, t1.codTipoDocumentacion))
        conn.commit()
        conn.close()