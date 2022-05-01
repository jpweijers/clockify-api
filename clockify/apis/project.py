from typing import List
from clockify.model.project_model import Project
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class ProjectWrapper(Wrapper):
    def get_projects(self, workspace_id: str) -> List[Project]:
        url = self.__url(workspace_id)
        return self.get_list(url, Project)

    def get_project(self, workspace_id: str, project_id: str) -> Project:
        url = self.__url(workspace_id, project_id)
        return self.get_one(url, Project)

    def create_project(self, project: Project) -> Project:
        url = self.__url(project.workspace_id, project.id_)
        return self.create_one(url, project, Project)

    def delete_project(self, workspace_id: str, project_id: str) -> Project:
        url = self.__url(workspace_id, project_id)
        return self.delete_one(url, Project)

    def update_project(self, project: Project) -> Project:
        url = self.__url(project.workspace_id, project.id_)
        return self.update_one(url, project, Project)

    def __url(self, workspace_id: str, project_id: str = None) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/projects"
        if project_id:
            url += f"/{project_id}"
        return url
