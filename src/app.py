import os
from enum import Enum
from r2r import (
    R2RConfig,
    R2RBuilder,
)

def r2r_app():
    config = R2RConfig.from_toml("r2r.toml")
    return R2RBuilder(config).build()

app = r2r_app().fapp
