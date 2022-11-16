""" Train params """

from dataclasses import dataclass, field


@dataclass()
class TrainingParams:
    """ Structure contains parameters for train data """
    model_type: str = field(default="LogisticRegression")
    random_state: int = field(default=42)
