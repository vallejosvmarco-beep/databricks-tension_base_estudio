# tension_base

Bundle (Declarative Automation Bundle) del proyecto tension_base.

## Origen de datos

Los datos de tension se leen del volumen de aterrizaje:

`/Volumes/datosami/datos/vol_alunizaje/ami/tension/`

Estructura: `source=AMI/format=PARQUET/periodo=AAAA/mes=M/r1|r2/*.parquet` (regiones r1 y r2; 2024-01 a 2026-10, 260 archivos, ~1.9 GB al 2026-11-20).

## Destino

Catalogo `datosami`, esquema existente `datos` (variables `catalog` y `schema`). No se crean esquemas ni volumenes: el usuario no tiene CREATE SCHEMA en `datosami`.

## Variables

* `catalog`: `datosami`
* `schema`: `datos`
* `tension_base_path`: `/Volumes/datosami/datos/vol_alunizaje/ami/tension/`
* `warehouse_id`: en `dev`, `fac1da9aa4b8e6dd` (Serverless Starter Warehouse)

## Uso

```bash
databricks bundle validate --target dev
databricks bundle deploy --target dev
databricks bundle run tension_base_initialize --target dev
```

El job `tension_base_initialize` solo verifica el esquema destino y lista el origen de tension.

## Pipeline `tension_base`

Pipeline (Lakeflow Spark Declarative Pipelines, serverless, triggered) con la tabla de streaming `datosami.datos.tension_base_bronce_tension`: ingesta incremental con Auto Loader (cada corrida solo lee parquet nuevos). Agrega `PERIODO`, `MES` (particiones), `REGION` (r1/r2), `ARCHIVO` y `FECHA_INGESTA`.

```bash
databricks bundle run tension_base --target dev
```

## Estructura

* `databricks.yml`: configuracion del bundle
* `resources/init.yml`: job `tension_base_initialize`
* `resources/tension_base.pipeline.yml`: pipeline `tension_base`
* `src/tension_base/transformations/bronce/tension_base_bronce_tension.py`: tabla bronce de tension
* `src/initialize`: notebook de verificacion del origen tension_base
* `src/initialize.sql`: SQL de verificacion usado por el job
