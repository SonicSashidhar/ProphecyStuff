from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "pf1", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    pf1__targetout = Process(name = "pf1__targetout", properties = ModelTransform(modelName = "pf1__targetout"))
    pf1__filter_2 = Process(name = "pf1__Filter_2", properties = ModelTransform(modelName = "pf1__Filter_2"))

