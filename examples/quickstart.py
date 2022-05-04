import clockify


KEY = "YOUR API KEY"

# create session
session = clockify.ClockifySession(KEY)
# get current user
current_user = session.get_current_user()

# get workspace ID from current user
workspace_id = current_user.active_workspace
print(workspace_id)

# Get clients
clients = session.client.get_clients(workspace_id)

if len(clients) > 0:
    print(clients[0])

    # change name
    clients[0].name = "McDonald's"

    # update client
    client = session.client.update_client(clients[0])

    print(client)

    # delete client
    session.client.delete(workspace_id, client.id_)

    # make query params to search for the deleted client
    params = clockify.ClientGetParams(name="McDonald's")

    # get clients with query params
    clients = session.client.get_clients(workspace_id, params)

    print(clients)
