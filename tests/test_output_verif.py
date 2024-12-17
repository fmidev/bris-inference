import numpy as np
import pytest


from bris.outputs.verif import Verif
from bris.sources.verif import Verif as VerifInput
from bris.predict_metadata import PredictMetadata

@pytest.fixture
def setup():
    stuff = 1
    yield stuff

def test_1():
    filename = "test.nc"
    sources = [VerifInput(filename)]

    variables = ["u_800", "u_600", "2t", "v_500", "10u"]
    lats = np.arange(50, 70)
    lons = np.arange(5, 15)
    leadtimes = [0, 6, 12, 18]
    num_members = 2
    thresholds = [0.2, 0.5]
    quantile_levels = [0.1, 0.9]

    field_shape = [len(lats), len(lons)]
    lats, lons = np.meshgrid(lats, lons)
    lats = lats.flatten()
    lons = lons.flatten()
    pm = PredictMetadata(variables, lats, lons, leadtimes, num_members, field_shape)
    ofilename = "otest.nc"
    workdir = "verif_workdir"
    output = Verif(pm, workdir, ofilename, "2t", "K", sources, thresholds=thresholds,
            quantile_levels=quantile_levels)

    frt = 1672552800
    for member in range(num_members):
        pred = np.random.rand(*pm.shape)
        output.add_forecast(frt, member, pred)

    output.finalize()


if __name__ == "__main__":
    test_1()
