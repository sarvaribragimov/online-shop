Folder Structure Conventions
============================

> Folder structure options and naming conventions for the current project

### A typical top-level directory layout

    .
    ├── .envs                   # Environment variables
    ├── requirements            # Third-party libraries
    ├── config                  # Project configuration files 
    ├── src                     # Project applications directory ('lib' or 'apps') 
    ├── static                  # Project static files directory 
    └── README.md               # About project

### SetUp 

- Install virtual environment:

```
git clone https://github.com/{repo}
cd root folder
python -m venv --prompt="v" .env
```

- If *pre commit* has not been installed please install by running following command:

```
pip install pre-commit
pre-commit install
```
