import dataclasses
import os
from random import randint
from enum import Enum
import json
from tkinter.tix import Tree
from clockify.dto import DTO
from clockify.client.client_dto import ClientDTO, ClientQueryDTO, SortColumn
from clockify.client.client_mapper import ClientQueryMapper
from clockify.model.project_model import Project
from clockify.session import ClockifySession

from clockify.wrapper import Wrapper

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


def get_client_query():
    q = ClientQueryDTO(sort_column=SortColumn.NAME)
    # client = session.get_clients(WORKSPACE, q)
    d = ClientQueryMapper().to_api(q)
    print(d)


def get_project():
    project = session.get_project(WORKSPACE, "6264286ef7a4597cbca48059")
    print(project)
    print("done")


def get_user():
    user = session.get_current_user()
    print(user)
    print("done")


def delete_project():
    project = Project(name=f"{randint(0,9999)}", workspace_id=WORKSPACE)
    project = session.create_project(project)
    project.archived = True
    project = session.update_project(project)
    project = session.delete_project(project.workspace_id, project.id_)
    print(project)
    pass


def delete_all_projects():
    projects = session.get_projects(WORKSPACE)
    for project in projects:
        project.archived = True
        session.update_project(project)
        session.delete_project(project.workspace_id, project.id_)


def delete_all_tags():
    tags = session.get_tags(WORKSPACE)
    print(tags)


if __name__ == "__main__":
    # delete_all_clients()
    # create_test_clients()
    # get_client_query()
    # get_project()
    # get_user()
    # print("/".join(["test", "api", None]))
    # delete_project()
    delete_all_projects()
    # delete_all_tags()


from clockify.session import ClockifySession

KEY = "YOUR_API KEY"
WORKSPACE = "YOUR WORKSPACE ID"

clockify_session = ClockifySession(KEY)

projects = clockify_session.project.get_projects(WORKSPACE)

for project in projects:
    print(f"Project {project.name}, Client: {project.client_name}")

clockify_session.client.delete_client("acv", "adfasdf")
