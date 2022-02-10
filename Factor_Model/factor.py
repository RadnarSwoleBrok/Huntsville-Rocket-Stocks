from API.requests.API_request import TDData
from value_factor import ValueFactor

from sklearn.decomposition import PCA
import seaborn
from abc import ABC, abstractmethod
from typing import Optional
from pydantic import dataclasses


@dataclasses
class Factor(ABC):
    """Represents a base factor model to be computed and displays relevant statistics"""

    value_factor: Optional[ValueFactor] = None
    momentum_factor: Optional[MomentumFactor] = None
    growth_factor: Optional[GrowthFactor] = None
    size_factor: Optional[SizeFactor] = None
    volatility_factor: Optional[VolatilityFactor] = None

    def __repr__(self):
        return f'factor.{self}'

    """Computes Principle Component Analysis for given set of factors"""
    @abstractmethod
    def computePCA(self):
        pass

    """Computes Factor Analysis for given set of factors"""
    @abstractmethod
    def computeFactorAnalysis(self):
        pass

    """Displays the results of the analysis in a seaborn graph"""
    @abstractmethod
    def displayAnalysis(self):
        pass






