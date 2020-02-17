"""SWF decisions making."""

import abc
import typing as t


class DecisionsBuilder(metaclass=abc.ABCMeta):
    """SWF decision builder.

    Args:
        workflow: workflow specification
        task: decision task
    """

    def __init__(self, workflow: "Workflow", task: t.Dict[str, t.Any]):
        self.workflow = workflow
        self.task = task
        self.decisions = []

    @abc.abstractmethod
    def build_decisions(self):  # pragma: no cover
        """Build decisions from workflow history."""
        raise NotImplementedError


class Workflow(metaclass=abc.ABCMeta):
    """SWF workflow specification.

    Args:
        spec: workflow specification
    """

    def __init__(self, spec: t.Dict[str, t.Any]):
        self.spec = spec

    @property
    @abc.abstractmethod
    def decisions_builder(self) -> DecisionsBuilder:  # pragma: no cover
        raise NotImplementedError

    @property
    @abc.abstractmethod
    def spec_type(self) -> str:  # pragma: no cover
        raise NotImplementedError

    def setup(self):
        """Set up workflow specification.

        Useful for pre-calculation or other initialisation.
        """

    def make_decisions(self, task: t.Dict[str, t.Any]) -> t.List[t.Dict[str, t.Any]]:
        """Build decisions from workflow history.

        Args:
            task: decision task

        Returns:
            workflow decisions
        """

        builder = self.decisions_builder(self, task)
        builder.build_decisions()
        return builder.decisions