# Databricks notebook source
# DBTITLE 1,Verificar origen tension_base
# tension_base: verifica el destino (datosami.datos) y el origen de datos de tension.
# No crea esquemas ni volumenes (se usan los existentes).
CATALOG = 'datosami'
SCHEMA = 'datos'
TENSION_BASE_PATH = '/Volumes/datosami/datos/vol_alunizaje/ami/tension/'

spark.sql(f'DESCRIBE SCHEMA `{CATALOG}`.`{SCHEMA}`').show(truncate=False)

origen = TENSION_BASE_PATH + 'source=AMI/format=PARQUET/'
periodos = sorted(f.name.strip('/') for f in dbutils.fs.ls(origen))
for p in periodos:
    meses = sorted(f.name.strip('/') for f in dbutils.fs.ls(origen + p + '/'))
    print(p, meses)
print(f'Origen tension_base: {TENSION_BASE_PATH}')