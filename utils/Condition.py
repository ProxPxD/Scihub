
class Condition:
    def __init__(self, condition):
        self._condition = condition

    def print(self, *msg, sep=' ', end='\n'):
        if self._condition:
            print(*msg, sep=sep, end=end)


def when(condition):
    return Condition(condition)
