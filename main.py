import pandas as pd
import numpy as np
import re
import os

# Rutas
input_folder = 'input'
output_folder = 'output'
files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

if not files:
    print("No se encontró ningún archivo CSV en la carpeta input/")
    exit()

input_file = files[0]
input_path = os.path.join(input_folder, input_file)

# Leer CSV (sin modificar encabezados)
df = pd.read_csv(input_path, encoding='utf-8-sig')
columnas_originales = df.columns.tolist() # Guardar encabezados originales

# Limpiar espacios vacíos antes de eliminar filas completamente vacías
df = df.apply(lambda col: col.map(lambda x: x.strip() if isinstance(x, str) else x))

df = df.replace('', None)  
df = df.dropna(how='all')

df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')


# Limpiar columna 'correo' si existe
if 'correo' in df.columns:
    df['correo'] = df['correo'].str.lower()
    
# Limpiar columna 'nombre' si existe
if 'nombre' in df.columns:
    df['nombre'] = df['nombre'].apply(lambda x: x.strip().title() if isinstance(x, str) else x)

# Restaurar los encabezados tal cual estaban
df.columns = columnas_originales

# Convertir a int si los números no tienen parte decimal
for col in df.select_dtypes(include=['float', 'int']).columns:
    df[col] = df[col].astype('Int64')  # Int

# Guardar CSV limpio
filename, ext = os.path.splitext(input_file)
output_file = f"{filename}_limpio.csv"
output_path = os.path.join(output_folder, output_file)

df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"Limpieza completada. Archivo exportado a: {output_path}")






