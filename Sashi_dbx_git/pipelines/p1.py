from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "p1", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    p1__filter_2 = Process(name = "p1__Filter_2", properties = ModelTransform(modelName = "p1__Filter_2"))
    p1__targetout = Process(name = "p1__targetout", properties = ModelTransform(modelName = "p1__targetout"))

