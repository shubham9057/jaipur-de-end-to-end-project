from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets
from .project import de_project

@dbt_assets(manifest=de_project.manifest_path)
def dbt_build(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    