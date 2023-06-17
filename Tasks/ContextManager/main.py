from contextlib import contextmanager
import sys
import traceback


@contextmanager
def supresser(*args):
    try:
        yield
    except Exception as exc:
        if isinstance(exc, args):
            return
        raise exc


@contextmanager
def retyper(type_from, type_to):
    try:
        yield
    except type_from as exc:
        exception = type_to()
        exception.args = exc.args
        raise exception


@contextmanager
def dumper(stream):
    try:
        yield
    except Exception as exc:
        stream.write(sys.exc_info()[1].args[0])
        raise sys.exc_info()[1]