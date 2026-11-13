from abc import ABC, abstractmethod
class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, order_total: float) -> float:
        pass