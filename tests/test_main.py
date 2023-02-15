import pytest

from main import IslandCounter, TerrainMapConverter


@pytest.fixture
def raw_input():
    return "0 0 0 0 0 0 0 0 0\n0 1 0 0 0 0 0 0 0\n1 1 1 0 0 0 1 0 0\n1 1 0 0 0 1 1 1 0\n0 0 0 0 0 1 1 0 0\n0 0 1 0 0 0 0 0 0\n1 1 0 0 0 0 0 0 0\n0 0 0 0 0 1 1 0 0\n"


def test_get_terrain_map(raw_input):
    terrain_map = TerrainMapConverter(raw_input).get_terrain_map()

    assert isinstance(terrain_map, list)
    assert len(terrain_map) == 8
    assert all([len(row) == 9 for row in terrain_map])
