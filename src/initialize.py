# Databricks notebook source
# Configure catalog and project name before running.
CATALOG = 'workspace'
PROJECT = 'project_base'
import re
for value in (CATALOG, PROJECT):
    if not re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', value):
        raise ValueError('Use simple SQL identifiers for catalog and project')
for schema in (PROJECT, f'{PROJECT}_bronze', f'{PROJECT}_silver', f'{PROJECT}_gold'):
    spark.sql(f'CREATE SCHEMA IF NOT EXISTS `{CATALOG}`.`{schema}`')
for volume in ('landing', 'metadata', 'sandbox'):
    spark.sql(f'CREATE VOLUME IF NOT EXISTS `{CATALOG}`.`{PROJECT}`.`{volume}`')
print(f'Landing: /Volumes/{CATALOG}/{PROJECT}/landing/')
