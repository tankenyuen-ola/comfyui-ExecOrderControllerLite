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