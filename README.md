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
├── app.py              # Punto d
```
