import importlib, traceback


def _load_class(cls_nm):
    """
    Dynamically load a class from a string

    :param cls_nm:
    :return:
    """
    class_data = cls_nm.split(".")
    module_path = ".".join(class_data[:-1])
    class_str = class_data[-1]

    module = importlib.import_module(module_path)
    return getattr(module, class_str)


def _getClass(system_key, cls_nm):

    cls_name = cls_nm.format(system_key)
    cls_obj = _load_class(cls_name)

    return cls_obj


class Factory:

    @staticmethod
    def getDataClass(system_key):
        cls_name = "sample_app.data_connections.{0}.data.Data"
        return _getClass(system_key, cls_name)


class APIModelError(Exception):
    pass


class MissingSystemKeyError(APIModelError):
    pass
