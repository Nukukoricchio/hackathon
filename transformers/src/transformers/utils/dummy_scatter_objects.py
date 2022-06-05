# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa
from ..utils import DummyObject, requires_backends


TAPAS_PRETRAINED_MODEL_ARCHIVE_LIST = None


class TapasForMaskedLM(metaclass=DummyObject):
    _backends = ["scatter"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["scatter"])


class TapasForQuestionAnswering(metaclass=DummyObject):
    _backends = ["scatter"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["scatter"])


class TapasForSequenceClassification(metaclass=DummyObject):
    _backends = ["scatter"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["scatter"])


class TapasModel(metaclass=DummyObject):
    _backends = ["scatter"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["scatter"])


class TapasPreTrainedModel(metaclass=DummyObject):
    _backends = ["scatter"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["scatter"])


def load_tf_weights_in_tapas(*args, **kwargs):
    requires_backends(load_tf_weights_in_tapas, ["scatter"])
