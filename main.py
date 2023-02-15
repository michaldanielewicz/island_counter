class InputReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_input(self) -> str:
        with open(self.file_path, "r") as f:
            terrain_input = f.read()
        return terrain_input


class TerrainMapConverter:
    def __init__(self, raw_input: str) -> None:
        self.raw_input = raw_input

    def get_terrain_map(self) -> list[list[int]]:
        terrain_map = []
        row = []
        for char in self.raw_input:
            try:
                land_or_water = int(char)
            except ValueError:
                pass
            else:
                row.append(land_or_water)
            if char == "\n":
                terrain_map.append(row)
                row = []
        return terrain_map


class IslandCounter:
    def __init__(self, terrain_map: list[list[int]]) -> None:
        self.terrain_map = terrain_map
