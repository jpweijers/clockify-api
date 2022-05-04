![GitHub Workflow Status](https://img.shields.io/github/workflow/status/jpweijers/clockify-api/CI)
[![Coverage Status](https://coveralls.io/repos/github/jpweijers/clockify-api/badge.svg?branch=main)](https://coveralls.io/github/jpweijers/clockify-api?branch=main)
[![Documentation Status](https://readthedocs.org/projects/clockify-api/badge/?version=latest)](https://clockify-api.readthedocs.io/en/latest/?badge=latest)

# Clockify

## Documentation

- [Package Documentation](clockify-api.readthedocs.io)
- [Official Clocify API reference](https://clockify.me/developers-api)

## Installation

```bash
# Pip
pip install clockify-api

# Poetry
poetry add clockify-api
```

## Example Usage

```python
from clockify.session import ClockifySession

KEY = "YOUR_API KEY"
WORKSPACE = "YOUR WORKSPACE ID"

clockify_session = ClockifySession(KEY)

projects = clockify_session.project.get_projects(WORKSPACE)

for project in projects:
    print(f"Project {project.name}, Client: {project.client_name}")
```
