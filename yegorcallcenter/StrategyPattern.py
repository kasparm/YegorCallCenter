import abc
import random


class Strategy(abc.ABC):
    def difficulty(self):
        pass


class ConcreteStrategyRandom(Strategy):
    def difficulty(self):
        return random.choice([0, 1, 2])


class ConcreteStrategyEasy(Strategy):
    def difficulty(self):
        return 0


class ConcreteStrategyHard(Strategy):
    def difficulty(self):
        return 2


class ConcreteStrategyRotate(Strategy):
    _current_difficulty = 0

    def difficulty(self):
        difficulty = self._current_difficulty
        self._current_difficulty += 1
        self._current_difficulty %= 3
        return difficulty


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self) -> Strategy:
        return self._strategy

    def difficulty(self):
        return self._strategy.difficulty()


if __name__ == "__main__":
    context = Context(ConcreteStrategyRandom())
    print("Difficulty: ", context.difficulty())


def test_easy():
    context = Context(ConcreteStrategyEasy())
    assert context.difficulty() == 0


def test_hard():
    context = Context(ConcreteStrategyHard())
    assert context.difficulty() == 2


def test_rotate():
    context = Context(ConcreteStrategyRotate())
    assert context.difficulty() == 0
    assert context.difficulty() == 1
    assert context.difficulty() == 2
    assert context.difficulty() == 0
