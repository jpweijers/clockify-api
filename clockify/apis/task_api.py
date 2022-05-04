from typing import List
from clockify.model.task_model import Task, TaskGetParams
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class TaskApi(Wrapper):
    def get_tasks(
        self,
        workspace_id: str,
        project_id: str,
        params: TaskGetParams = TaskGetParams(),
    ) -> List[Task]:
        """Get list of Task object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            project_id (str): ID of the clockify project.
            params (TaskGetParams, optional): Path parameters. Defaults to TaskGetParams().

        Returns:
            List[Task]: List of Task objects.
        """
        url = self.__url(workspace_id, project_id)
        return self._get_list(url, Task, params)

    def get_task(self, workspace_id: str, project_id: str, task_id: str) -> Task:
        """Return one Task object

        Args:
            workspace_id (str): ID of the clockify workspace.
            project_id (str): ID of the clockify project.
            task_id (str): ID of the clockify task.

        Returns:
            Task: Task object.
        """
        url = self.__url(workspace_id, project_id, task_id)
        return self._get_one(url, Task)

    def create_task(self, workspace_id: str, task: Task) -> Task:
        """Create a task and return it as a Task object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            task (Task): Task to create.

        Returns:
            Task: Created Task object.
        """
        url = self.__url(workspace_id, task.project_id, task.id_)
        return self._create_one(url, task, Task)

    def delete_task(self, workspace_id: str, project_id: str, task_id: str) -> Task:
        """Delete a task and return it as a Task object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            project_id (str): ID of the clockify project.
            task_id (str): ID of the clockify task.

        Returns:
            Task: Deleted Task object.
        """
        url = self.__url(workspace_id, project_id, task_id)
        return self._delete_one(url, Task)

    def update_task(self, workspace_id: str, task: Task) -> Task:
        """Update a task and return it as a Task object.

        Args:
            workspace_id (str): ID of the clockify workspace.
            task (Task): Task to update.

        Returns:
            Task: Updated Task object.
        """
        url = self.__url(workspace_id, task.project_id, task.id_)
        return self._update_one(url, task, Task)

    def __url(self, workspace_id: str, project_id: str, task_id: str = None) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/projects/{project_id}/tasks"
        if task_id:
            url += f"/{task_id}"
        return url
