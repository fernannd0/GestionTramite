from config.database import conectar
from models.TipoTramite import TipoTramite
class TipoTramiteRespositorio:
        
    """
    Esta funcion puede devolver un None(si no encuentra nada), un TipoTramite(si solo encuentra uno) o una lista:TipoTramite(si encuentra mas de uno) 
    """
    def buscarTipoTramite(self, busqueda):  
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        patron=f"%{busqueda}%"
        cursor.execute("""
            SELECT *
            FROM TipoTramite
            WHERE codTipoTramite=%s OR nombreTipoTramite LIKE %s;
        """, (busqueda, patron,))
        r=cursor.fetchall()
        conn.close()
        if isinstance(busqueda, int):
            a=r[0]
            return TipoTramite(a["nombreTipoTramite"], a["cantidadDiasMaximoDocumentacion"], a["codTipoTramite"], a["fechaHoraBajaTT"])
        resultadott=[TipoTramite(res["nombreTipoTramite"], res["cantidadDiasMaximoDocumentacion"], res["codTipoTramite"], res["fechaHoraBajaTT"])for res in r]
        return resultadott
    
    def darAltaTipoTramite(self, t1:TipoTramite):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            INSERT INTO TipoTramite (nombreTipoTramite, cantidadDiasMaximoDocumentacion)
            VALUES (%s, %s);

        """, (t1.nombreTipoTramite, t1.cantidadDiasMaximoDocumentacion))
        conn.commit()
        conn.close()
    
    def traerTodosTipoTramite(self):
        conn=conectar()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT *
            FROM TipoTramite
            ORDER BY fechaHoraBajaTT ASC;
        """)
        resultado=cursor.fetchall()
        resultadott=[TipoTramite(r["nombreTipoTramite"], r["cantidadDiasMaximoDocumentacion"], r["codTipoTramite"], r["fechaHoraBajaTT"]) for r in resultado]
        conn.close()
        return resultadott

    def actualizarTipoTramite(self, t1:TipoTramite):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE TipoTramite
            SET nombreTipoTramite=%s,
                cantidadDiasMaximoDocumentacion=%s
            WHERE codTipoTramite=%s;
        """, (t1.nombreTipoTramite, t1.cantidadDiasMaximoDocumentacion, t1.codTipoTramite))
        conn.commit()
        conn.close()

    def darBajaTipoTramite(self, t1:TipoTramite):
        conn=conectar()
        cursor=conn.cursor()
        cursor.execute("""
            UPDATE TipoTramite
            SET fechaHoraBajaTT=%s
            WHERE codTipoTramite=%s;
        """, (t1.fechaHoraBajaTT, t1.codTipoTramite))
        conn.commit()
        conn.close()
