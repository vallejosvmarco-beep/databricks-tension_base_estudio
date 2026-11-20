from pyspark import pipelines as dp
from pyspark.sql import functions as F

# =============================================================
# tension_base - BRONCE TENSION
# =============================================================
# Ingesta incremental con Auto Loader desde el volumen de aterrizaje:
#   /Volumes/datosami/datos/vol_alunizaje/ami/tension/
#   source=AMI/format=PARQUET/periodo=AAAA/mes=M/r1|r2/*.parquet
# Cada corrida solo lee los archivos parquet nuevos (los ya ingeridos
# no se vuelven a leer). Se conservan las columnas tal como vienen en el
# parquet y se agregan PERIODO y MES (de la ruta), REGION (r1/r2 de la
# ruta), ARCHIVO y FECHA_INGESTA para trazabilidad.
# =============================================================

TABLA = "tension_base_bronce_tension"


@dp.table(
    name=TABLA,
    comment="tension_base bronce: lecturas de tension AMI (parquet de vol_alunizaje/ami/tension), ingesta incremental con Auto Loader.",
    partition_cols=["PERIODO", "MES"],
    table_properties={"delta.enableRowTracking": "true"},
)
def tension_base_bronce_tension():
    origen = spark.conf.get("tension_base.path").rstrip("/") + "/source=AMI/format=PARQUET/"
    return (
        spark.readStream.format("cloudFiles")
        .option("cloudFiles.format", "parquet")
        .option("cloudFiles.partitionColumns", "periodo,mes")
        .load(origen)
        .withColumnRenamed("periodo", "PERIODO")
        .withColumnRenamed("mes", "MES")
        .withColumn("REGION", F.regexp_extract(F.col("_metadata.file_path"), r"/(r\d+)/", 1))
        .withColumn("ARCHIVO", F.col("_metadata.file_path"))
        .withColumn("FECHA_INGESTA", F.current_timestamp())
    )
