import traceback
import sys


def force_load(module):
    ldict = {}
    with open(module + '.py') as f:
        mod = f.readlines()
    while True:
        try:
            exec(''.join(mod), globals(), ldict)
            break
        except SyntaxError as se:
            mod.pop(se.lineno - 1)
        except Exception as exc:
            tb = traceback.extract_tb(sys.exc_info()[2])
            mod.pop(tb[-1][1] - 1)
    return ldict
