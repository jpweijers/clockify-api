# Clockify

[![Coverage Status](https://coveralls.io/repos/github/jpweijers/clockify-api/badge.svg?branch=main)](https://coveralls.io/github/jpweijers/clockify-api?branch=main)

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
