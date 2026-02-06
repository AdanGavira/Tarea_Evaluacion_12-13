# Proyecto: Automatización de Carga de Datos (CSV a PostgreSQL/Odoo)

Este proyecto demuestra cómo actuar como desarrollador para automatizar la entrada de datos externos en un motor de ERP (Odoo), utilizando **Python** como puente de conexión.

## 🛠️ Procedimiento de Configuración y Ejecución

Se han seguido los siguientes pasos técnicos para garantizar la integración exitosa:

### 1. Preparación del Entorno
* [cite_start]**Instalación de Python:** Se descargó la versión estable de [python.org](https://www.python.org/downloads/), asegurando marcar la casilla **"Add Python to PATH"** durante la instalación[cite: 228, 238].
* **Librerías Necesarias:** Se instalaron los conectores y herramientas de gestión de datos mediante la terminal:
    ```bash
    pip install psycopg2-binary pandas
    ```
    * **Psycopg2:** Funciona como el driver de conexión (equivalente al JDBC de Java).
    * **Pandas:** Utilizado para la carga masiva y eficiente del archivo CSV.

### 2. Infraestructura Docker
* Se levantó un entorno con tres contenedores vinculados: **Odoo**, **PostgreSQL (db)** y **pgAdmin**.
* Se verificó la red del contenedor mediante:
    ```bash
    docker inspect db --format "{{json .NetworkSettings.Networks}}"
    ```

### 3. Ejecución del Script de Automatización
El script de Python realiza las siguientes acciones críticas:
* **Carga con Pandas:** Lee el archivo `listado.csv` de golpe en un DataFrame, gestionando tildes con `encoding='latin1'`.
* **Conexión Segura:** Utiliza un diccionario de parámetros para conectar con el host `localhost` en el puerto `5432`.
* **Creación de Tabla (DDL):** Asegura la existencia de la tabla `contactos_mailing` usando tipos `TEXT` para máxima flexibilidad.
* **Inserción Masiva:** Recorre el archivo e inserta los datos usando marcadores `%s` para evitar inyección SQL.
* **Gestión Transaccional (ACID):** Se implementó un sistema de `commit()` para guardar cambios y `rollback()` en caso de error para evitar la corrupción de datos.

## 📸 Evidencias de Éxito

> La siguiente captura muestra la terminal de VS Code con el mensaje de confirmación ("¡Éxito! Se han importado 10 contactos"), la ventana de pgAdmin con los datos cargados y el reloj del sistema visible.

<img width="888" height="174" alt="Captura de pantalla 2026-02-06 122853" src="https://github.com/user-attachments/assets/6fb9bef1-79ed-43d7-a205-3af2bee761e4" />

<img width="1365" height="648" alt="Captura de pantalla 2026-02-06 123307" src="https://github.com/user-attachments/assets/c67317a5-0a9f-49ab-a1be-8cb87ba94100" />

## 📊 Comparativa Técnica (Java vs Python)

| Concepto | Java (JDBC) | Python (Psycopg2 + Pandas) |
| :--- | :--- | :--- |
| **Lectura** | BufferedReader + bucle while |`pd.read_csv()` (una línea)  |
| **Estructura** | Bloques `{ }` y `;` | Indentación (espacios)  |
| **Seguridad** | PreparedStatement (`?`) | Marcador `%s` |

## 👤 Autor
* **Adan Gavira Palacios** - [AdanGavira](https://github.com/AdanGavira)
