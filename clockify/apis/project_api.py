from typing import List
from clockify.model.project_model import Project, ProjectGetParams
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class ProjectApi(Wrapper):
    def get_projects(
        self, workspace_id: str, params: ProjectGetParams = ProjectGetParams()
    ) -> List[Project]:
        """Return list of Project objects.

        Args:
            workspace_id (str): ID of the clockify workspace.
            params (ProjectGetParams, optional): Path parameters. Defaults to ProjectGetParams().

        Returns:
            List[Project]: List of Project Objects
        """
        url = self.__url(workspace_id)
        return self._get_list(url, Project, params)

    def get_project(self, workspace_id: str, project_id: str) -> Project:
        """Return one Project object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            project_id (str): ID of the clockify project.

        Returns:
            Project: Project object.
        """
        url = self.__url(workspace_id, project_id)
        return self._get_one(url, Project)

    def create_project(self, project: Project) -> Project:
        """Create one Project and return it as a Project object.

        Args:
            project (Project): Clockify Project to create.

        Returns:
            Project: Created Project object.
        """
        url = self.__url(project.workspace_id, project.id_)
        return self._create_one(url, project, Project)

    def delete_project(self, workspace_id: str, project_id: str) -> Project:
        """Delete a Project and return it as a Project object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            project_id (str): ID of the clockify project.

        Returns:
            Project: Deleted Project object.
        """
        url = self.__url(workspace_id, project_id)
        return self._delete_one(url, Project)

    def update_project(self, project: Project) -> Project:
        """Update a Project and return it as a Project object.

        Args:
            project (Project): Project to update.

        Returns:
            Project: Updated Project object.
        """
        url = self.__url(project.workspace_id, project.id_)
        return self._update_one(url, project, Project)

    def __url(self, workspace_id: str, project_id: str = None) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/projects"
        if project_id:
            url += f"/{project_id}"
        return url
