# ExecOrderControllerLite/exec_order_controller.py
# ANY = ("*",)  # ComfyUI's wildcard type

# class ExecOrderControllerLite:
#     """
#     Passthrough node to force an execution edge without bringing Impact-Pack deps.
#     """

#     @classmethod
#     def INPUT_TYPES(cls):
#         return {
#             "required": {
#                 "signal": (ANY,),   # anything just to create a dependency edge
#                 "value":  (ANY,),   # the payload you care about
#             }
#         }

#     RETURN_TYPES = (ANY, ANY)
#     RETURN_NAMES = ("signal", "value")
#     FUNCTION = "doit"
#     CATEGORY = "Util/Lite"

#     def doit(self, signal, value):
#         # Simply return both so downstream nodes pull them (and thus enforce order)
#         return signal, value

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_typ = AnyType("*")

class ImpactExecutionOrderController:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
                    "signal": (any_typ,),
                    "value": (any_typ,),
                    }}

    FUNCTION = "doit"

    CATEGORY = "ImpactPack/Util"
    RETURN_TYPES = (any_typ, any_typ)
    RETURN_NAMES = ("signal", "value")

    def doit(self, signal, value):
        return signal, value