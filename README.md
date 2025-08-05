

## 📌 Descripción

Este script automatiza la limpieza de archivos CSV: elimina filas vacías, normaliza nombres y correos, restaura encabezados originales y exporta un nuevo archivo limpio.

🔹 Entrada: un archivo CSV con datos a limpiar (colócalo en la carpeta input/).
🔹 Salida: un archivo CSV limpio en la carpeta output/.


---

## 📂 Estructura del proyecto
```plaintext
Proyecto/
├── input/           # Coloca aquí tu archivo CSV original
├── output/          # Aquí se guardará el archivo CSV limpio
├── main.py          # Script principal de limpieza
├── requirements.txt # Dependencias necesarias
└── README.md        # Este archivo
```

---

## ✅ Requisitos

1️⃣ Python 3.10 o superior
🔗 Descargar Python

> Durante la instalación, asegúrate de marcar ✅ Add Python to PATH




---

🔧 Instalación de dependencias

Se recomienda usar un entorno virtual para aislar tus dependencias:

### Crear entorno virtual (solo la primera vez)
*python -m venv venv*

### Activar entorno virtual

### En Windows:
venv\Scripts\activate

### En macOS/Linux:
source venv/bin/activate

### Instalar dependencias
*pip install -r requirements.txt*

> Contenido de requirements.txt:

pandas
numpy


---

## ▶️ Ejecución del script

Una vez activado el entorno virtual y colocados tus archivos CSV en la carpeta input/, ejecuta:

*python main.py*

El script procesará el primer archivo CSV encontrado en input/ y generará el archivo limpio en la carpeta output/, con el mismo nombre pero terminado en _limpio.csv.


---

##🚨 Notas importantes

✅ El script limpia los encabezados solo internamente para trabajar mejor, pero restaura los encabezados originales en el archivo final.
✅ Se eliminan filas completamente vacías y se limpian columnas como correo y nombre si existen.
✅ Convierte a enteros las columnas numéricas sin decimales.


---

## 📄 Licencia

Este proyecto se entrega como ejemplo para automatización de limpieza de datos. Puedes adaptarlo libremente para tus necesidades.


---

¿Te gustaría que te prepare los comandos para subir este README actualizado a tu repositorio?

---

## 🤝 Autor

### Oscar Alegre
💼 Especialista en Automatización con Python.
📧 Contacto: (oscaralregre19@gmail.com)
