# Great Expectations Demo Integration with DataHub

This repository demonstrates the integration of **Great Expectations** with **DataHub**, providing examples of data validation for both CSV files and PostgreSQL databases.

## Setup Instructions

- Clone the repository:
```
git clone https://github.com/sarubhai/great_expectations_demo.git
cd great_expectations_demo
```
- Set Up the Virtual Environment:
Refer to [this guide](https://appdev24.com/pages/30/setup-python-project-on-macos) for instructions on setting up a Python virtual environment on macOS.

```
python3.11 -m venv env
```

- Activate the virtual environment:
```
source env/bin/activate
```

- Upgrade pip and install dependencies:
```
pip install --upgrade pip
pip install -r requirements.txt
```

## Integration with DataHub
To explore DataHub integration, use the [Data Governance Demo repository](https://github.com/sarubhai/data-governance-demo).
Below is the Great Expectations Action for Datahub:

```
action_list:
  - name: datahub_action
    action:
      module_name: datahub_gx_plugin.action
      class_name: DataHubValidationAction
      server_url: http://localhost:8080
      token: ${DATAHUB_ACCESS_TOKEN}
      env: PROD
      exclude_dbname: False
      platform_alias: postgres
      graceful_exceptions: True
      parse_table_names_from_sql: True
      convert_urns_to_lowercase: True
```

## Setup Environment Variables
```
export POSTGRES_CONNECTION_STRING="postgresql+psycopg2://postgres:P%40ssw0rd%21234@localhost:5432/postgres"
export DATAHUB_DEBUG=true
export DATAHUB_ACCESS_TOKEN=None
```
## Run Great Expectations Checkpoints

### For CSV Files (Pandas + Filesystem Integration)
```
cd pandas_filesystem_csv
python run_gx_checkpoint.py
```

### For PostgreSQL (SQLAlchemy Integration)
```
cd ../postgres_sqlalchemy
python run_gx_postgres_checkpoint.py
```

## Deactivate the Virtual Environment
```
deactivate
```


## Screenshots
#### Dathub GX Integration
![Dathub GX Integration](images/gx-datahub-int.png)