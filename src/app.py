import os
from enum import Enum
from r2r import (
    R2RConfig,
    R2RAppBuilder,
    # For Web Search
    WebSearchPipe,
    SerperClient,
    get_r2r_app,
    # For HyDE & the like.
    R2RPipeFactoryWithMultiSearch
)


class RagPipeline(Enum):
    QNA = "qna"
    WEB = "web"
    HYDE = "hyde"

def r2r_app():
    rag_pipeline = RagPipeline(os.getenv("RAG_PIPELINE", "qna"))
    
    config = R2RConfig.from_json("config.json")

    if rag_pipeline == RagPipeline.QNA:
        return get_r2r_app(R2RAppBuilder(config))
    elif rag_pipeline == RagPipeline.WEB:
        # Create search pipe override and pipes
        web_search_pipe = WebSearchPipe(
            serper_client=SerperClient()  # TODO - Develop a `WebSearchProvider` for configurability
        )
        return get_r2r_app(R2RAppBuilder(config).with_search_pipe(web_search_pipe))
    elif rag_pipeline == RagPipeline.HYDE:
        return get_r2r_app(R2RAppBuilder(config).with_pipe_factory(R2RPipeFactoryWithMultiSearch), task_prompt_name="hyde")

app = r2r_app().app
