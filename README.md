# README

This directory contains the necessary files to deploy a basic RAG pipeline using the R2R framework with the SciPhi cloud platform.

## File Structure

The main files in this directory are:

- `src/app.py`: The main entry point for the application.
- `config.json`: The configuration file used to control the deployment settings.
- `requirements.txt`: The file specifying the Python dependencies required by the application.

## Application Overview

The application is built using the `r2r` library and follows a pipeline-based architecture. The main entry point is in the `src/app.py` file, which creates a pipeline using the `E2EPipelineFactory.create_pipeline()` method. This method reads the configuration settings from the `config.json` file to set up the various components of the pipeline.

The `config.json` file contains the following configuration options:

- `database`: Specifies the vector database provider. In this case, the default is set to "sciphi". This results in a SciPhi managed Lantern database. Selecting an alternative provider like `qdrant` allows the developer to connect with their remote cloud offering.
- `evals`: Specifies the evaluation provider (set to "deepeval") and the pipeline evaluation frequency.
- `embedding`: Specifies the embedding provider (set to "openai"), the embedding model, dimension, and batch size.
- `text_splitter`: Specifies the text splitting settings, including the chunk size and chunk overlap.
- `language_model`: Specifies the language model provider. In this case, it is set to "litellm".

## Configuration

The `config.json` file is used to control the deployment settings of the application. You can modify the configuration options in this file to customize the behavior of the pipeline components, such as the database provider, continuous evaluation settings, embedding settings, text splitter settings, and language model provider.