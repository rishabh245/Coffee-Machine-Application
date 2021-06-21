from task_manager.task import Task


class TaskQueue:

    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_full(self):
        if len(self.queue) == self.size:
            return True

        return False

    def is_empty(self):
        return len(self.queue) == 0

    def add_task(self, task: Task):
        if self.is_full():
            return False

        self.queue.append(task)
        return True

    def get_first_task(self):
        if not self.is_empty():
            task = self.queue.pop(0)
            return task

    def clear(self):
        self.queue = []
