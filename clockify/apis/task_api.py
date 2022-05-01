from typing import List
from clockify.model.task_model import Task
from clockify.config import BASE_URL
from clockify.wrapper import Wrapper


class TaskWrapper(Wrapper):
    def get_tasks(self, workspace_id: str, project_id: str) -> List[Task]:
        url = self.__url(workspace_id, project_id)
        return self.get_list(url, Task)

    def get_task(self, workspace_id: str, project_id: str, task_id: str) -> Task:
        url = self.__url(workspace_id, project_id, task_id)
        return self.get_one(url, Task)

    def create_task(self, workspace_id: str, task: Task) -> Task:
        url = self.__url(workspace_id, task.project_id, task.id_)
        return self.create_one(url, task, Task)

    def delete_task(self, workspace_id: str, project_id: str, task_id: str) -> Task:
        url = self.__url(workspace_id, project_id, task_id)
        return self.delete_one(url, Task)

    def update_task(self, workspace_id: str, task: Task) -> Task:
        url = self.__url(workspace_id, task.project_id, task.id_)
        return self.update_one(url, task, Task)

    def __url(self, workspace_id: str, project_id: str, task_id: str = None) -> str:
        url = f"{BASE_URL}/workspaces/{workspace_id}/projects/{project_id}/tasks"
        if task_id:
            url += f"/{task_id}"
        return url
