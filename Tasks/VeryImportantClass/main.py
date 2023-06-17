from app import VeryImportantClass, decorator
import collections.abc


class HackedClass(VeryImportantClass):

    def __getattribute__(self, name):

        attr = super().__getattribute__(name)

        if not name[0] == '_':

            if isinstance(attr, int) or isinstance(attr, float):
                return attr * 2

            elif isinstance(attr, collections.abc.Container):
                return type(attr)()

            elif callable(attr):
                return decorator(attr)

        return attr
