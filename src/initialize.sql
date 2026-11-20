-- Replace placeholders using the deployment script before running this SQL.
-- This file is a reference SQL template; use src/initialize.py in a notebook
-- if SQL task variable substitution is unavailable.
CREATE SCHEMA IF NOT EXISTS workspace.project_base;
CREATE VOLUME IF NOT EXISTS workspace.project_base.landing;
CREATE VOLUME IF NOT EXISTS workspace.project_base.metadata;
CREATE VOLUME IF NOT EXISTS workspace.project_base.sandbox;
CREATE SCHEMA IF NOT EXISTS workspace.project_base_bronze;
CREATE SCHEMA IF NOT EXISTS workspace.project_base_silver;
CREATE SCHEMA IF NOT EXISTS workspace.project_base_gold;
