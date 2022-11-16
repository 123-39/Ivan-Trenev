""" Splitting params """

from dataclasses import dataclass, field


@dataclass
class SplittingParams:
    """ Structure contains parameters for splitting data """
    test_size: float = field(default=0.15)
    random_state: int = field(default=42)
