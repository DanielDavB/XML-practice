import mysql.connector
import xml.dom.minidom as minidom

# Configura la conexión a la base de datos MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'ejemplo_xml_db'
}

# Conecta a la base de datos
try:
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Consulta la base de datos y obtén los registros
    cursor.execute("SELECT id, nombre, salario FROM empleados")
    empleados = cursor.fetchall()

    # Crea el documento XML
    doc = minidom.Document()
    root = doc.createElement("empleados")
    doc.appendChild(root)

    # Genera elementos XML para cada empleado
    for empleado in empleados:
        empleado_elem = doc.createElement("empleado")

        id_elem = doc.createElement("id")
        id_elem.appendChild(doc.createTextNode(str(empleado[0])))
        empleado_elem.appendChild(id_elem)

        nombre_elem = doc.createElement("nombre")
        nombre_elem.appendChild(doc.createTextNode(empleado[1]))
        empleado_elem.appendChild(nombre_elem)

        salario_elem = doc.createElement("salario")
        salario_elem.appendChild(doc.createTextNode(str(empleado[2])))
        empleado_elem.appendChild(salario_elem)

        root.appendChild(empleado_elem)

    # Guarda el XML en un archivo
    with open("empleados.xml", "w") as xml_file:
        xml_file.write(doc.toprettyxml(indent="  "))

    print("Archivo XML generado con éxito: empleados.xml")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn:
        conn.close()
