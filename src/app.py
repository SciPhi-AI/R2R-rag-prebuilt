import os
from enum import Enum
from r2r import (
    R2RConfig,
    R2RBuilder,
    # For Web Search
    WebSearchPipe,
    SerperClient,
    # For HyDE & the like.
    R2RPipeFactoryWithMultiSearch
)


class RagPipeline(Enum):
    QNA = "qna"
    WEB = "web"
    HYDE = "hyde"

def r2r_app():
    
    config = R2RConfig.from_toml("r2r.toml")
    return R2RBuilder(config).build().app

app = r2r_app().app
