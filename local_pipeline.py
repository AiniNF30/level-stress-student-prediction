"""
Author: Aini Nurpadilah
Date: 10/01/2025
This is the local_pipeline.py
Usage:
- Run the ML pipeline components
"""

import os
from typing import Text

from absl import logging
from tfx.orchestration import metadata, pipeline
from tfx.orchestration.beam.beam_dag_runner import BeamDagRunner

PIPELINE_NAME = "stress-pipeline"

# Pipeline inputs
DATA_ROOT = "data"
TRANSFORM_MODULE_FILE = "modules/transform.py"
TRAINER_MODULE_FILE = "modules/trainer.py"

# Pipeline outputs
OUTPUT_BASE = "output"
SERVING_MODEL_DIR = os.path.join(OUTPUT_BASE, 'serving_model')
PIPELINE_ROOT = os.path.join(OUTPUT_BASE, PIPELINE_NAME)
METADATA_PATH = os.path.join(PIPELINE_ROOT, "metadata.sqlite")


def init_local_pipeline(
    pipeline_components, root_dir: Text
) -> pipeline.Pipeline:
    """
    Initializes a TFX pipeline with BeamDagRunner.

    Args:
        pipeline_components (list): A list of pipeline components.
        root_dir (Text): The root directory for pipeline outputs.

    Returns:
        pipeline.Pipeline: A configured TFX pipeline instance.
    """
    logging.info(f"Pipeline root set to: {root_dir}")
    beam_args = [
        "--direct_running_mode=multi_processing",
        "--direct_num_workers=0"  # Auto-detect based on available CPUs
    ]

    return pipeline.Pipeline(
        pipeline_name=PIPELINE_NAME,
        pipeline_root=root_dir,
        components=pipeline_components,
        enable_cache=True,
        metadata_connection_config=metadata.sqlite_metadata_connection_config(
            METADATA_PATH
        ),
        beam_pipeline_args=beam_args
    )


if __name__ == "__main__":
    logging.set_verbosity(logging.INFO)

    from modules.components import init_components

    pipeline_components = init_components(
        DATA_ROOT,
        training_module=TRAINER_MODULE_FILE,
        transform_module=TRANSFORM_MODULE_FILE,
        training_steps=5000,
        eval_steps=1000,
        serving_model_dir=SERVING_MODEL_DIR,
    )

    pipeline_instance = init_local_pipeline(pipeline_components, PIPELINE_ROOT)
    BeamDagRunner().run(pipeline=pipeline_instance)
