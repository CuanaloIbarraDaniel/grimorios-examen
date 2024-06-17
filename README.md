# AI Software Grimorios


## Requisitos

- [Python 3.12.X](https://www.python.org/downloads/) Instalado
- [PostgreSQL 16.x](https://www.postgresql.org/) Instalado

## Tecnologías

- Lenguaje: [Python 3.12.2](https://www.python.org/downloads/)
- Framework: [FastAPI](https://fastapi.tiangolo.com/) + [Piccolo](https://piccolo-orm.readthedocs.io/en/latest/index.html)
- Base de Datos: [PostgreSQL](https://www.postgresql.org/)
- Pruebas: [PyTest](https://docs.pytest.org/en/8.2.x/)
- Documentación: [Swagger](https://swagger.io/)

## Setup

&nbsp;
## 1.- Crear base de datos principal 
El primer paso es crear la base de datos para producción dento de PostgreSQL debido a que todavía no existe una forma para hacerlo dentro del programa.

```bash
CREATE DATABASE grimorios
```

## 2.- Crear base de datos de pruebas 
El siguiente paso es crear la base de datos para las pruebas dentro de PostgreSQL.

```bash
CREATE DATABASE grimorios_test
```

## 3.- Instalar dependencias
Acto seguido se debe instalar todos los modulos requeridos

```bash
pip install -r requirements.txt
```

## 4.- Configurar settings.py
Una vez realizado el acto anterior ahora se debe configurar el archivo settings dentro de settings.py para establecer la base de datos y los otras conexiones

```bash
Host: str = "127.0.0.1" # Host donde va a correr FastAPI
Port: int = 8470 # Puerto donde va a correr FastAPI
Environment: str = "" # Ambiente de desarrollo/producción de la aplicación
AppLogLevel: LogLevel = LogLevel.INFO # Establecel nivel mínimo de la app
DatabaseHost: str = "localhost" # Host de la base de datos
DatabasePort: int = 5432 # Puerto de la base de datos
DatabaseUsername: str = "" # Usuario de la base de datos
DatabasePassword: str = "" # Contraseña de la base de datos
DatabaseName: str = "" # Nombre de la base de datos
DatabaseNameTest: str = "" # Nombre de la base de datos de prueba
```

## 5.- Creación de tablas
Se deben correr las migraciones para poder crear las tablas

```bash
piccolo migrations forwards database
```

## 5.- Agregar datos a las tablas
Acto siguiente se debe correr la migración para agregar datos a la base de datos

```bash
piccolo migrations forwards database_data
```
## Correr APP

## A.- Ejecutar la aplicación
Esto se realiza dentro de la carpeta "grimorios"

```bash
python main.py
```

## B.- Ejecutar las pruebas
Esto se realiza dentro de la carpeta "grimorios"

```bash
piccolo tester run
```

## Documentación

## A.- Postman
En el folder principal del proyecto puedes encontrar una colección de Postman en la carpeta nombrada "postman"

## B.- Swagger
All ejecutar la aplicación podrás acceder a los Docs de Swagger agregando la palabra "docs" al final del enlace generado por la aplicación