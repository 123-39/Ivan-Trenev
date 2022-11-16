
""" Feature params """

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class FeatureParams:
    """ Structure contains categorical and numerical params in dataset"""
    categorical_features: List[str]
    numerical_features: List[str]
    target_col: Optional[str]
