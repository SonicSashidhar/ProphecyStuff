from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "pf2", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    pf2__filter_2 = Process(name = "pf2__Filter_2", properties = ModelTransform(modelName = "pf2__Filter_2"))
    pf2__targetout = Process(name = "pf2__targetout", properties = ModelTransform(modelName = "pf2__targetout"))

