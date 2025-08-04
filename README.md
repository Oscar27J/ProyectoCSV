# Proyecto 02 - Limpieza automática de datos CSV

Este script permite limpiar automáticamente archivos CSV con errores comunes como datos vacíos, duplicados o texto inconsistente.

---

## 🔧 ¿Qué hace?

- Elimina filas vacías y duplicadas
- Rellena valores nulos con datos por defecto
- Corrige errores de formato de texto (capitalización)
- Exporta un nuevo archivo limpio listo para análisis

---

## 📂 Estructura del proyecto

Proyecto_02_LimpiezaCSV/
│
├── input/ # Archivos CSV originales
│ └── datos_ventas.csv
│
├── output/ # Archivos CSV limpios
│ └── datos_ventas_limpio.csv
│
├── main.py # Script principal
├── requirements.txt # Dependencias
└── README.md # Instrucciones

## ▶️ ¿Cómo se usa?

1. Ejecuta el script:

bash
    pip install -r requirements.txt


2. Coloca tu archivo .csv en la carpeta input/ con el nombre datos_ventas.csv.

3. Ejecuta el script:
    python main.py

4. El archivo limpio estará en la carpeta output/.

🧠 Requisitos
Python 3.8 o superior

Librería pandas

📬 ¿Tienes un archivo que necesita limpieza?
Este script puede adaptarse a cualquier archivo CSV. Solo necesitas enviarlo y yo me encargo del resto.