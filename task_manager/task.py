import abc


class Task(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        """
         Task execution implementation
        """
