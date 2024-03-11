"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd


def leer_columna(linea: str, inicio: int) -> str:
    col = ""
    for i in range(inicio, len(linea)):
        if linea[i] == " ":
            break
        col += linea[i]
    return col


def ingest_data():
    with open('clusters_report.txt', 'r') as file:

        data = []
        skiprows = 4
        filas = []

        for row, line in enumerate(file):
            if row < skiprows:
                continue
            if line.strip() == '':
                continue

            data.append(line)
            cluster = leer_columna(line, 3)
            if cluster == "":
                continue

            cant_palabras = leer_columna(line, 9)
            cant_porcentaje_palabras = leer_columna(line, 25).replace(",", ".")
            filas.append([cluster, cant_palabras, cant_porcentaje_palabras])

            col1 = [int(row[0]) for row in filas]
            col2 = [int(row[1]) for row in filas]
            col3 = [float(row[2]) for row in filas]

        palabras_claves = []
        todas_palabras_claves = ""
        with open('clusters_report.txt', 'r') as file:
            for row, line in enumerate(file):
                if row < skiprows:
                    continue
                if line.strip() == '':
                    continue

                line = line.strip("\n")
                # palabras_claves.append(line[41:].split(", "))
                todas_palabras_claves += line[41:] + " "

        for palabras in todas_palabras_claves.split("."):
            palabras_claves.append(palabras)

        df = pd.DataFrame({
            "Cluster": col1,
            "Cantidad de palabras clave": col2,
            "Porcentaje de palabras clave": col3,
            "Principales palabras clave": palabras_claves[:-1]
        })

        df.columns = df.columns.str.lower().str.replace(" ", "_")
        df['principales_palabras_clave'] = df['principales_palabras_clave'].str.replace(r"\s{2,}", " ", regex=True).str.strip()


    return df



