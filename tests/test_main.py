import pytest

from main import IslandCounter, TerrainMapConverter


@pytest.fixture
def raw_input():
    return "0 0 0 0 0 0 0 0 0\n0 1 0 0 0 0 0 0 0\n1 1 1 0 0 0 1 0 0\n1 1 0 0 0 1 1 1 0\n0 0 0 0 0 1 1 0 0\n0 0 1 0 0 0 0 0 0\n1 1 0 0 0 0 0 0 0\n0 0 0 0 0 1 1 0 0\n"


@pytest.fixture
def island_counter(raw_input):
    terrain_map = TerrainMapConverter(raw_input).get_terrain_map()
    return IslandCounter(terrain_map)


def test_get_terrain_map(raw_input):
    terrain_map = TerrainMapConverter(raw_input).get_terrain_map()

    assert isinstance(terrain_map, list)
    assert len(terrain_map) == 8
    assert all([len(row) == 9 for row in terrain_map])


@pytest.mark.parametrize("invalid_input", ["0 0 1 2 0", "12 0 0 1"])
def test_check_input_is_valid(invalid_input):
    with pytest.raises(ValueError):
        TerrainMapConverter(invalid_input)


def test_check_input_is_not_empty():
    with pytest.raises(ValueError):
        TerrainMapConverter(raw_input="")


def test_is_out_of_map(island_counter):
    assert island_counter._is_out_of_map(10, 10) is True
    assert island_counter._is_out_of_map(-1, 0) is True
    assert island_counter._is_out_of_map(0, -1) is True
    assert island_counter._is_out_of_map(-100, -100) is True
    assert island_counter._is_out_of_map(5, 5) is False
    assert island_counter._is_out_of_map(0, 1) is False


def test_is_land(island_counter):
    assert island_counter._is_land(0, 0) is False
    assert island_counter._is_land(0, 7) is False
    assert island_counter._is_land(7, 0) is False
    assert island_counter._is_land(5, 5) is False
    assert island_counter._is_land(1, 1) is True
    assert island_counter._is_land(3, 1) is True


def test_count_islands(island_counter):
    assert island_counter.count_islands() == 4

    terrain_map = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    island_counter.set_terrain_map(terrain_map=terrain_map)
    assert island_counter.count_islands() == 0

    terrain_map = [
        [0, 1, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    island_counter.set_terrain_map(terrain_map=terrain_map)
    assert island_counter.count_islands() == 1

    terrain_map = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    island_counter.set_terrain_map(terrain_map=terrain_map)
    assert island_counter.count_islands() == 1

    terrain_map = [
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 0, 1]
    ]
    island_counter.set_terrain_map(terrain_map=terrain_map)
    assert island_counter.count_islands() == 4

    terrain_map = [
        [1, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
    ]
    island_counter.set_terrain_map(terrain_map=terrain_map)
    assert island_counter.count_islands() == 3

    terrain_map = [[1]]
    island_counter.set_terrain_map(terrain_map=terrain_map)
    assert island_counter.count_islands() == 1

    terrain_map = [[0]]
    island_counter.set_terrain_map(terrain_map=terrain_map)
    assert island_counter.count_islands() == 0


