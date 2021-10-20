from models.reflex import ReflexModel
from models.attentive import AttentiveModel
from models.modular import ModularModel
from models.modular_ac import ModularACModel
from models.keyboard import KeyboardModel

def load(config):
    cls_name = config.model.name
    try:
        cls = globals()[cls_name]
        return cls(config)
    except KeyError:
        raise Exception("No such model: {}".format(cls_name))
