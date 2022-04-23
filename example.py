import dataclasses
import os
from random import randint
from clockify.client.client_dto import ClientDTO
from clockify.session import ClockifySession

KEY = os.environ.get("API_KEY")
WORKSPACE = os.environ.get("WORKSPACE")

client = ClientDTO("1234", "Test", "abcd", "abcd", "test")
session = ClockifySession(KEY)

# res = session.create_client(WORKSPACE, client)
# print(res)


def delete_all_clients():
    clients = session.get_clients(WORKSPACE)
    for client in clients:
        session.delete_client(WORKSPACE, client.id_)


def create_test_clients():
    clients = [f"Test Client #{i}" for i in range(1, 11)]
    for client in clients:
        client = ClientDTO(client)
        session.create_client(WORKSPACE, client)


if __name__ == "__main__":
    delete_all_clients()
    # create_test_clients()
