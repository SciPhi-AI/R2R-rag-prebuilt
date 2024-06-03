import os
import logging
from enum import Enum
from r2r import (
    R2RConfig,
    R2RAppBuilder,
    # For Web Search
    R2RWebSearchPipe,
    SerperClient,
    # For HyDE & the like.
    R2RPipeFactoryWithMultiSearch
)

logger = logging.getLogger(__name__)

current_file_path = os.path.dirname(__file__)

class RagPipeline(Enum):
    QNA = "qna"
    WEB = "web"
    HYDE = "hyde"

def r2r_app( rag_pipeline: RagPipeline = RagPipeline.QNA):
    config = R2RConfig.from_json("config.json")

    if rag_pipeline == RagPipeline.QNA:
        return R2RAppBuilder(config).build()
    elif rag_pipeline == RagPipeline.WEB:
        # Create search pipe override and pipes
        web_search_pipe = R2RWebSearchPipe(
            serper_client=SerperClient()  # TODO - Develop a `WebSearchProvider` for configurability
        )
        return R2RAppBuilder(config).with_search_pipe(web_search_pipe).build()
    elif rag_pipeline == RagPipeline.HYDE:
        return R2RAppBuilder(config).with_pipe_factory(R2RPipeFactoryWithMultiSearch) \
            .build(
                # Add optional override arguments which propagate to the pipe factory
                task_prompt_name="hyde",
            )
