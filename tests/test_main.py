from main import TerrainMapConverter


def test_get_terrain_map(raw_input):
    terrain_map = TerrainMapConverter(raw_input).get_terrain_map()

    assert isinstance(terrain_map, list)
    assert len(terrain_map) == 8
    assert all([len(row) == 9 for row in terrain_map])
