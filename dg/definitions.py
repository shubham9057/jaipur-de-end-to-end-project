from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import dbt_build
from .project import de_project
from .schedules import schedules

defs = Definitions(
    assets=[dbt_build],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=de_project),
    },
)