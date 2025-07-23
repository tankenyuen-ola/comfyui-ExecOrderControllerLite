# ExecOrderControllerLite/__init__.py
from .exec_order_controller import ImpactExecutionOrderController

NODE_CLASS_MAPPINGS = {
    "ExecOrderControllerLite": ImpactExecutionOrderController,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExecOrderControllerLite": "Execution Order Controller (Lite)",
}