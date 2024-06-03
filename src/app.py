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
configs_path = os.path.join(current_file_path, "..", "..", "..")

CONFIG_OPTIONS = {
    "default": None,
    "local_ollama": os.path.join(configs_path, "local_ollama.json"),
}

class RagPipeline(Enum):
    QNA = "qna"
    WEB = "web"
    HYDE = "hyde"

def r2r_app(config_name: str = "default", rag_pipeline: RagPipeline = RagPipeline.QNA):
    if config_path := CONFIG_OPTIONS.get(config_name):
        logger.info(f"Using config path: {config_path}")
        config = R2RConfig.from_json(config_path)
    else:
        default_config_path = os.path.join(configs_path, "config.json")
        logger.info(f"Using default config path: {default_config_path}")
        config = R2RConfig.from_json(default_config_path)

    if config.embedding.provider == 'openai' and 'OPENAI_API_KEY' not in os.environ:
        raise ValueError("Must set OPENAI_API_KEY in order to initialize OpenAIEmbeddingProvider.")

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
