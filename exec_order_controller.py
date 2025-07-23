# ExecOrderControllerLite/exec_order_controller.py
from nodes import ANY  # ComfyUI's built-in "any" type

class ExecOrderControllerLite:
    """
    Passthrough node to force an execution edge without bringing Impact-Pack deps.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "signal": (ANY,),   # anything just to create a dependency edge
                "value":  (ANY,),   # the payload you care about
            }
        }

    RETURN_TYPES = (ANY, ANY)
    RETURN_NAMES = ("signal", "value")
    FUNCTION = "doit"
    CATEGORY = "Util/Lite"

    def doit(self, signal, value):
        # Simply return both so downstream nodes pull them (and thus enforce order)
        return signal, value