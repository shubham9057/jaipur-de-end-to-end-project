# jaipur-de-end-to-end-project
Data Engineering DBT project with Snowflake using dagster and other tools.


# Contributing
## Environment Setup
1. Install uv: [https://docs.astral.sh/uv/getting-started/installation/#installing-uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv)
    - We use uv for python versioning and package management because it enables more consistent environments across contributors.
2. Clone this repo
    - If you're already contributing and were previously using pyenv or rye with a locally activated virtualenv, you'll need to deactivate it and delete it.
3. From the [root directory](.), run:
    1. `uv sync` - to install dependencies defined in [pyproject.toml](pyproject.toml) to the uv project
    2. `uv venv` - to create a virtual environment  
    3. `source .venv/bin/activate` - to activate the virtualenv so installed modules are directly callable. You may skip this step and call packages via uv: `uv run <module>`   
4. Configure dbt-snowflake connection
    1. The [dbt/profiles.yml](./dbt/profiles.yml) file defines the target connections using environment variables. Those environment variables must exist in your environment when you run dbt. There are many ways to accomplish this. The approach below describes using the [VS Code Integrated Terminal environment variables](https://docs.myaltimate.com/setup/optConfig/#environment-variables-setup-using-the-integrated-terminal-profiles-vscodesettingsjson).
    1. In your VS Code User Settings (Code > Settings... > Settings):
    2. Search "terminal integrated env"; click `Edit in settings.json` for your respective OS. 
    3. Add these variables:   
        > "SNOWFLAKE_ACCOUNT": "<your_account_id>",  
        "SNOWFLAKE_WAREHOUSE": "<your_warehouse>",  
        "SNOWFLAKE_ROLE": "<your_role>",  
        "SNOWFLAKE_USERNAME": "<your_username>",  
        "SNOWFLAKE_DATABASE": "<your_database>",  
        "SNOWFLAKE_SCHEMA": "<your_schema>"    
    2. Restart your VS Code Terminal for changes to take effect
    3. Validate results from the [dbt](/dbt/) directory, run:  
        `dbt debug` - to verify connection  
        `dbt deps` - to install dbt packages
5. To add new python dependencies, run:  
   `uv add <module>` or `uv add "<module>==<version>"`  
    - Again run `uv sync` to install them.
