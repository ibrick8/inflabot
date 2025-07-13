from abc import ABC, abstractmethod

from domain.entidades.PosteoEntity import PosteoEntity

class IUseCase(ABC):
    @abstractmethod
    def run(self, posteo: PosteoEntity): pass
