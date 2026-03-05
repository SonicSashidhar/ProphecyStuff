from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "pf1f2", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    pf1f2__filter_2 = Process(name = "pf1f2__Filter_2", properties = ModelTransform(modelName = "pf1f2__Filter_2"))
    pf1f2__targetout = Process(name = "pf1f2__targetout", properties = ModelTransform(modelName = "pf1f2__targetout"))

