import numpy as np
import os


from bris.sources.verif import Verif
from bris import source


def test_instantiate():
    filename = os.path.dirname(os.path.abspath(__file__)) + "/files/verif_input.nc"
    args = {"filename": filename}

    obs_source = source.instantiate("verif", args)


if __name__ == "__main__":
    test_instantiate()
