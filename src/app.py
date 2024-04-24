import os
from r2r.main import E2EPipelineFactory, R2RConfig

# Loads the local configuration file
config = R2RConfig.load_config("config.json")

env_setting = os.getenv("RAG_PIPELINE", None)

# Selects the pipeline to use
rag_pipeline = env_setting or config.app.get("rag_pipeline", "qna")
if rag_pipeline == "qna":
    from r2r.pipelines import QnARAGPipeline
    rag_pipeline_impl = QnARAGPipeline
elif rag_pipeline == "web":
    from r2r.pipelines import WebRAGPipeline
    rag_pipeline_impl = WebRAGPipeline
elif rag_pipeline == "agent":
    from r2r.pipelines import AgentRAGPipeline
    rag_pipeline_impl = AgentRAGPipeline
elif rag_pipeline == "hyde":
    from r2r.pipelines import HyDEPipeline
    rag_pipeline_impl = HyDEPipeline
else:
    raise ValueError(f"Invalid pipeline: {rag_pipeline}")

app = E2EPipelineFactory.create_pipeline(config=config, rag_pipeline_impl=rag_pipeline_impl)