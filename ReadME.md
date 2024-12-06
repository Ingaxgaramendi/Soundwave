# 🎶 SoundWave CRUD 🎟️  

**SoundWave CRUD** es una aplicación interactiva desarrollada en **Python** que permite gestionar la venta de entradas para conciertos, festivales y eventos deportivos. Implementa un sistema completo **CRUD (Crear, Leer, Actualizar, Eliminar)** utilizando Programación Orientada a Objetos (POO) y una estructura modular para asegurar escalabilidad y facilidad de uso.

---

## 📋 **Tabla de Contenidos**

- [Características](#✨-características)
- [Estructura del Proyecto](#📂-estructura-del-proyecto)
- [Instalación](#⚙️-instalación)
- [Uso](#🚀-uso)
- [Tecnologías](#🛠️-tecnologías)
- [Capturas](#📸-capturas)


---

## ✨ **Características**

# -*- coding: utf-8 -*-

1. **CRUD Completo**:
   - Crear eventos: Conciertos, Festivales y Eventos Deportivos.
   - Leer eventos: Mostrar todos los registros o buscar por ID.
   - Actualizar eventos: Editar detalles como nombre, fecha, precio, etc.
   - Eliminar eventos: Borrar registros existentes.

2. **Validaciones Robustas**:
   - ID único por evento.
   - Verificación de campos no vacíos y formato correcto.

3. **Modularidad**:
   - Código dividido en módulos según la funcionalidad.

4. **POO Aplicada**:
   - Clases personalizadas con herencia (`Concert`, `Festival`, `SportEvent`).

5. **Datos Iniciales**:
   - Base de datos simulada con eventos precargados.

---

## 📂 **Estructura del Proyecto**

```
SoundWaveCRUD/
├── main.py            # Archivo principal para ejecutar el programa
├── models/            # Módulo que contiene los modelos de eventos
│   ├── event_models.py
├── utils/             # Módulo de utilidades para validaciones
│   ├── validators.py
├── iu/                # Módulo de interfaz de usuario
│   ├── menu.py
├── database/          # Datos iniciales del sistema
│   ├── data.py
└── README.md          # Documentación del proyecto
```

---

## ⚙️ **Instalación**

# Guía para ejecutar el código desde GitHub

Sigue estos pasos para clonar y ejecutar el código de este repositorio en tu PC.

## 1. Instalar Git
Si no tienes Git instalado, descárgalo desde [aquí](https://git-scm.com/downloads) y sigue las instrucciones.

## 2. Clonar el repositorio
Abre la terminal o línea de comandos y ejecuta el siguiente comando:

```bash
git clone https://github.com/usuario/repositorio.git

---

**Pasos para ejecutar un código de GitHub sin tener Git instalado:**

**1. Descargar el código desde GitHub**

Ve al repositorio de GitHub que deseas ejecutar.
Haz clic en el botón verde "Code" y selecciona "Download ZIP".
Esto descargará el repositorio como un archivo comprimido .zip en tu PC.

**2. Descomprimir el archivo ZIP**

Una vez descargado el archivo .zip, descomprímelo en una carpeta de tu elección.
**3. Instalar Python**

Si no tienes Python instalado en tu PC, ve a la página oficial de Python y sigue las instrucciones para instalarlo. Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.

**4. Abrir la terminal o línea de comandos**
Dependiendo de tu sistema operativo:

Windows: Abre "Símbolo del sistema" o "PowerShell".
macOS/Linux: Abre la terminal.

**5. Navegar a la carpeta del repositorio**
Una vez que hayas descomprimido el archivo .zip, abre la terminal y usa el comando cd para navegar a la carpeta donde descomprimiste el repositorio. Por ejemplo:

```bash
Copiar código
cd ruta/del/repositorio
Reemplaza ruta/del/repositorio con la ruta correcta de la carpeta en tu PC.

ejm:
C:\Users\Alumno\Downloads\SOUNDWAVE DATA BASE

## 🚀 **Uso**

1. **Ejecuta la aplicación**:
   ```bash
   python main.py
   ```

2. **Interfaz interactiva**:
   - Usa las opciones del menú principal para gestionar eventos:
     - Mostrar todos los eventos.
     - Buscar un evento por ID.
     - Crear, actualizar o eliminar eventos.

3. **Ejemplo de menú**:
   ```
   === Menú Principal ===
   1. Mostrar todos los eventos 📋
   2. Buscar evento por ID 🔍
   3. Agregar un nuevo evento ➕
   4. Actualizar un evento ✏️
   5. Eliminar un evento 🗑️
   6. Comprar entradas
   7. Salir 🚪
   Ingrese una opción:
   ```

---
- **Casos de prueba**: He documentado los casos de prueba en el `README.md`, explicando qué hace cada uno y cómo ejecutarlos. Para cada caso de prueba, he proporcionado un bloque de código que muestra cómo se realiza la prueba.
- **Instrucciones**: Se indican los pasos necesarios para ejecutar las pruebas con `unittest`.

### Ejecución de las pruebas

Al ejecutar `python -m unittest test.py`, se ejecutarán todos los métodos de prueba que estén definidos en el archivo `test.py`. Asegúrate de que tu archivo `test.py` tenga una estructura similar a esta:
```python

import unittest
from models.event_models import create_event, read_event, update_event, delete_event, buy_ticket
from database.data import events
from utils.validators import validate_name

class TestSoundWaveCRUD(unittest.TestCase):

    def test_create_event(self):
       # Definir prueba para crear evento

    def test_read_event(self):
        # Definir prueba para leer evento

    def test_update_event(self):
       # Definir prueba para actualizar evento
    def test_delete_event(self):
      # Definir prueba para eliminar evento


    def test_buy_ticket_valid(self):
      # Definir prueba para comprar ticket

    def test_buy_ticket_invalid(self):
        

if __name__ == "__main__":
    unittest.main()
```
## 📸 **Capturas Caso de prueba** 

![image](https://github.com/user-attachments/assets/f3b6d8ef-7175-4423-bb8e-aee075e34a63)

## 🛠️ **Tecnologías**

- **Lenguaje**: Python 3.8+
- **Paradigma**: Programación Orientada a Objetos (POO)
- **Estructura**: Modular

---

## 📸 **Capturas**

### Menú Principal  
![image](https://github.com/user-attachments/assets/0d503346-8cb5-4594-9db2-557cf5a271d9)


### Crear Evento  
![image](https://github.com/user-attachments/assets/69ac043a-d601-4148-9a79-e2828ced5234)



