# GastoBot

Bot de Telegram desarrollado en Python para la gestión de gastos personales y vencimientos automáticos.

El proyecto permite registrar gastos, organizar categorías, consultar resúmenes y administrar vencimientos con recordatorios automáticos enviados directamente por Telegram.

---

# Características

* Registro de gastos personales
* Categorías personalizadas por usuario
* Resumen mensual de gastos
* Gestión de vencimientos
* Recordatorios automáticos
* Persistencia en MySQL
* Integración con Docker
* Dashboard de monitoreo con Grafana
* Arquitectura modular por capas
* Migraciones con Flask-Migrate y Alembic

---

# Tecnologías utilizadas

## Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Migrate
* SQLAlchemy
* APScheduler

## Base de datos

* MySQL

## Infraestructura

* Docker
* Docker Compose
* Grafana
* phpMyAdmin

## Integraciones

* Telegram Bot API

---

# Arquitectura del proyecto

```text
GastoBot/
│
├── models/             # Modelos ORM
├── routes/             # Endpoints y webhooks
├── services/           # Lógica de negocio
├── jobs/               # Tareas programadas
├── utils/              # Utilidades auxiliares
├── migrations/         # Migraciones Alembic
├── database.py         # Configuración de SQLAlchemy
├── config.py           # Variables de configuración
├── app.py              # Punto de entrada
├── requirements.txt
└── docker-compose.yml
```

---

# Funcionalidades principales

## Gestión de gastos

Permite registrar gastos indicando:

* descripción
* monto
* categoría
* fecha

También permite:

* eliminar gastos
* validar montos
* evitar duplicados
* listar categorías registradas
* generar resúmenes mensuales

---

## Gestión de vencimientos

Los usuarios pueden registrar vencimientos como:

* luz
* internet
* alquiler
* tarjeta

El sistema:

* almacena la fecha de vencimiento
* calcula días restantes
* indica vencimientos próximos
* envía recordatorios automáticos

---

## Recordatorios automáticos

El proyecto utiliza APScheduler para ejecutar tareas programadas.

Cada cierto intervalo:

1. Se consultan vencimientos pendientes
2. Se calcula la diferencia de días
3. Se envían alertas automáticas por Telegram
4. Se marca el vencimiento como avisado

---

# Variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=gastos
MYSQL_PASSWORD=gastos1
MYSQL_DATABASE=misgastosbot

TELEGRAM_TOKEN=TU_TOKEN

GRAFANA_USER=admin
GRAFANA_PASSWORD=admin
GRAFANA_URL=http://localhost:3000
GRAFANA_DASHBOARD_ID=dashboard_id
```

---

# Instalación local

## 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd GastoBot
```

---

## 2. Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno virtual:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Levantar servicios Docker

```bash
docker compose up -d
```

Servicios incluidos:

* MySQL
* phpMyAdmin
* Grafana

---

## 5. Ejecutar migraciones

```bash
flask db upgrade
```

---

## 6. Ejecutar aplicación

```bash
python app.py
```

---

# Comandos del bot

| Comando                | Descripción           |
| ---------------------- | --------------------- |
| `/gasto`               | Registrar un gasto    |
| `/categorias`          | Listar categorías     |
| `/resumen`             | Ver resumen mensual   |
| `/eliminar`            | Eliminar gasto        |
| `/vencimiento`         | Registrar vencimiento |
| `/vencimientos`        | Listar vencimientos   |
| `/eliminarvencimiento` | Eliminar vencimiento  |

---

# Base de datos

El proyecto utiliza SQLAlchemy como ORM y Flask-Migrate/Alembic para versionado de esquema.

Migraciones:

```bash
flask db migrate -m "descripcion"
flask db upgrade
```

---

# Monitoreo

Grafana disponible en:

```text
http://localhost:3000
```

phpMyAdmin disponible en:

```text
http://localhost:8080
```

---

# Buenas prácticas implementadas

* Arquitectura modular
* Separación de responsabilidades
* Variables de entorno
* Migraciones versionadas
* Timezone explícita para Argentina
* Scheduler desacoplado
* Validaciones de entrada
* Prevención de duplicados
* Relaciones ORM

---

# Roadmap

* [ ] Exportación Excel/PDF
* [ ] Dashboard web
* [ ] Tests automatizados
* [ ] API REST
* [ ] Categorización automática de gastos
* [ ] Deploy en la nube

---

# Autor

Marisol Torres

Analista de Sistemas y estudiante de Ingeniería en Sistemas de Información.

Desarrolladora Full Stack orientada al desarrollo backend y aplicaciones web.
