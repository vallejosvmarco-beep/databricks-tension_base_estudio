# Universal Databricks Free Edition foundation

Reusable GitHub template for a Unity Catalog landing volume and medallion schemas.

## Important

Free Edition capabilities and quotas vary. This template uses an **existing** catalog (`workspace` by default) and assumes permissions to create schemas and managed volumes. It does not create a catalog, compute, or warehouse. Databricks Asset Bundles deployment requires Databricks CLI authentication. A GitHub repository alone does not automatically deploy resources.

## Recommended first-time setup (Free Edition)

1. Create a GitHub repository using this folder as a template.
2. Open the repository in a Databricks Git folder, or import `src/initialize.py` into your workspace.
3. Set `CATALOG` and `PROJECT` in the notebook, then run it using available compute.
4. Upload source files to `/Volumes/<catalog>/<project>/landing/`.
5. Ask your available Databricks AI coding assistant to create the ingestion pipeline and Delta tables. Genie is generally for querying data, not provisioning pipelines.

## Bundle CLI path (where supported)

The bundle includes a SQL initialization job, but its SQL is an **example** with fixed `workspace.project_base` names. Edit `src/initialize.sql` to match your project before deployment. Set a valid existing SQL warehouse ID and authenticate the CLI:

```bash
databricks bundle validate --var warehouse_id=<SQL_WAREHOUSE_ID>
databricks bundle deploy --var warehouse_id=<SQL_WAREHOUSE_ID>
databricks bundle run initialize_foundation --var warehouse_id=<SQL_WAREHOUSE_ID>
```

`bundle deploy` deploys the job definition; `bundle run` executes initialization. The CLI route depends on an available SQL warehouse and permissions; the notebook route is the recommended fallback.

## Suggested AI prompt

Read CSV/Parquet files in `/Volumes/workspace/project_base/landing/`, infer schemas, create append-safe bronze Delta tables in `workspace.project_base_bronze`, track source filename and ingestion timestamp, quarantine malformed rows, and explain the generated pipeline before execution. Never delete landing files without approval.

## Layout

- `databricks.yml`: bundle settings
- `resources/init.yml`: optional SQL initialization job
- `src/initialize.py`: recommended Free Edition initialization notebook
- `src/initialize.sql`: example SQL initialization script
