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
    rag_pipeline = RagPipeline(os.getenv("RAG_PIPELINE", "qna"))
    
    config = R2RConfig.from_toml("config.toml")

    if rag_pipeline == RagPipeline.QNA:
        return R2RBuilder(config).build().app
    elif rag_pipeline == RagPipeline.WEB:
        # Create search pipe override and pipes
        web_search_pipe = WebSearchPipe(
            serper_client=SerperClient()  # TODO - Develop a `WebSearchProvider` for configurability
        )
        return R2RBuilder(config).with_vector_search_pipe(web_search_pipe).build().app
    elif rag_pipeline == RagPipeline.HYDE:
        return R2RBuilder(config).with_pipe_factory(R2RPipeFactoryWithMultiSearch) \
            .build(
                # Add optional override arguments which propagate to the pipe factory
                task_prompt_name="hyde",
            ).app

app = r2r_app().app
