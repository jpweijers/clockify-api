from clockify import session
from clockify.model.client_model import ClientGetParams

KEY = "YOUR API KEY"

# Create Session
clockify_session = session.ClockifySession(KEY)

# Get current user
current_user = clockify_session.get_current_user()

# Get clients
params = ClientGetParams(archived=False)
clients = clockify_session.client.get_clients(current_user.active_workspace, params)
for client in clients:
    print(client)

# Update a project
project = clockify_session.project.get_project(
    workspace_id=current_user.active_workspace, project_id="your_projec_id"
)
project.name = "Updated Name"
updated_project = clockify_session.project.update_project(project)
