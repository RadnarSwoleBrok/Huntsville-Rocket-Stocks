from pydantic import dataclasses
from Factor_Model.factor import Factor
import pandas as pd
from typing import Optional

@dataclasses
class ValueFactor(Factor):

    ROICdata: Optional[pd.DataFrame] = None



