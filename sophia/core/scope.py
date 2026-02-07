from enum import Enum

class Realm(Enum):
    CABIN = "cabin"
    MARKET = "market"
    VOID = "void"
    GLOBAL = "global"

class Layer(Enum):
    SURFACE = "surface"
    DEEP = "deep"
    AKASHIC = "akashic"

class Topic(Enum):
    GENERAL = "general"
    MARKET = "market"
    CODE = "code"
    RITUAL = "ritual"

class FrequencyTuner:
    """
    Compiles the 'Scope String'. Ensures we know WHERE we are.
    Enforces Canonical Purity via the Enum Lock protocol.
    """
    @staticmethod
    def tune(realm: Realm, layer: Layer = Layer.SURFACE, topic: Topic = Topic.GENERAL):
        # Returns a rigid, searchable path
        # Example: "realm:cabin/layer:surface/topic:general"
        
        # Enforce Enum types
        if not isinstance(realm, Realm):
            raise TypeError(f"Invalid Realm type: {type(realm)}. Must be {Realm}")
        if not isinstance(layer, Layer):
            raise TypeError(f"Invalid Layer type: {type(layer)}. Must be {Layer}")
        if not isinstance(topic, Topic):
            raise TypeError(f"Invalid Topic type: {type(topic)}. Must be {Topic}")
            
        return f"realm:{realm.value}/layer:{layer.value}/topic:{topic.value}"
