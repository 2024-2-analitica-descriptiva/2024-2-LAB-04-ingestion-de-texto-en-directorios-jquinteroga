# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

"""

def pregunta_01():

La información requerida para este laboratio esta almacenada en el
archivo "files/input.zip" ubicado en la carpeta raíz.
Descomprima este archivo.

Como resultado se creara la carpeta "input" en la raiz del
repositorio, la cual contiene la siguiente estructura de archivos:


```
train/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
test/
    negative/
        0000.txt
        0001.txt
        ...
    positive/
        0000.txt
        0001.txt
        ...
    neutral/
        0000.txt
        0001.txt
        ...
```

A partir de esta informacion escriba el código que permita generar
dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
del repositorio.

Estos archivos deben tener la siguiente estructura:

* phrase: Texto de la frase. hay una frase por cada archivo de texto.
* sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
    o "neutral". Este corresponde al nombre del directorio donde se
    encuentra ubicado el archivo.

Cada archivo tendria una estructura similar a la siguiente:

```
|    | phrase                                                                                                                                                                 | target   |
|---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
|  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
|  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
|  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
|  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
|  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
```


"""

import zipfile
import os
import pandas as pd

def pregunta_01():

    # Definición de rutas
    zip_path = "files/input.zip"
    input_dir = "input"
    output_dir = "files/output"

    # Descomprimir el archivo zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall()

    # Crear directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def process_files(folder, output_file):
        data = []
        for sentiment in ["negative", "neutral", "positive"]:
            sentiment_folder = f"{folder}/{sentiment}"

            if not os.path.exists(sentiment_folder):
                continue

            for file_name in os.listdir(sentiment_folder):
                file_path = os.path.join(sentiment_folder, file_name)
                if file_name.endswith(".txt"):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            phrase = f.read().strip()
                            data.append({"phrase": phrase, "target": sentiment})
                    except Exception as e:
                        print(f"Error leyendo el archivo {file_path}: {e}")

        # Guardar el dataset en formato CSV
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False, encoding='utf-8')
        print(f"Archivo {output_file} generado exitosamente.")

    # Procesar conjuntos de entrenamiento y prueba
    process_files(f"{input_dir}/train", f"{output_dir}/train_dataset.csv")
    process_files(f"{input_dir}/test", f"{output_dir}/test_dataset.csv")

pregunta_01()

