"""
    Conexión a SQLServer con Python
    Ejemplo de CRUD evitando inyecciones SQL
     
    @author parzibyte

    Más tutoriales en:
                        parzibyte.me/blog
"""
import pyodbc
direccion_servidor = 'DESKTOP-OJ9C4FV'
nombre_bd = 'pruebas_parzibyte'
nombre_usuario = 'user'
password = 'user'
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    # OK! conexión exitosa
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)
