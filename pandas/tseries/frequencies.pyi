#from pandas._libs.algos import unique_deltas as unique_deltas
#from pandas._libs.tslibs import Timedelta as Timedelta, Timestamp as Timestamp
#from pandas._libs.tslibs.ccalendar import MONTH_ALIASES as MONTH_ALIASES, int_to_weekday as int_to_weekday
#from pandas._libs.tslibs.fields import build_field_sarray as build_field_sarray
#from pandas._libs.tslibs.resolution import Resolution as Resolution
#from pandas._libs.tslibs.timezones import UTC as UTC
#from pandas._libs.tslibs.tzconversion import tz_convert as tz_convert
#from pandas.core.algorithms import unique as unique
#from pandas.core.dtypes.common import is_datetime64_dtype as is_datetime64_dtype, is_period_arraylike as is_period_arraylike, is_timedelta64_dtype as is_timedelta64_dtype
#from pandas.core.dtypes.generic import ABCSeries as ABCSeries
from pandas.tseries.offsets import DateOffset as DateOffset
# , Day as Day, Hour as Hour, Micro as Micro, Milli as Milli, Minute as Minute, Nano as Nano, Second as Second
#from pandas.util._decorators import cache_readonly as cache_readonly
from typing import Any, Optional

def get_period_alias(offset_str: str) -> Optional[str]: ...
def to_offset(freq: Any) -> Optional[DateOffset]: ...
def get_offset(name: str) -> DateOffset: ...
def infer_freq(index: Any, warn: bool=...) -> Optional[str]: ...

class _FrequencyInferer:
    index: Any = ...
    values: Any = ...
    warn: Any = ...
    is_monotonic: Any = ...
    def __init__(self, index: Any, warn: bool=...) -> None: ...
    def deltas(self): ...
    def deltas_asi8(self): ...
    def is_unique(self) -> bool: ...
    def is_unique_asi8(self): ...
    def get_freq(self) -> Optional[str]: ...
    def day_deltas(self): ...
    def hour_deltas(self): ...
    def fields(self): ...
    def rep_stamp(self): ...
    def month_position_check(self): ...
    def mdiffs(self): ...
    def ydiffs(self): ...

class _TimedeltaFrequencyInferer(_FrequencyInferer): ...