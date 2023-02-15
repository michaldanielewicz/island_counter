class InputReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_input(self) -> str:
        """Reads an input from a file and return it as a string."""
        with open(self.file_path, "r") as f:
            terrain_input = f.read()
        return terrain_input


class TerrainMapConverter:
    def __init__(self, raw_input: str) -> None:
        self.raw_input = raw_input

    def get_terrain_map(self) -> list[list[int]]:
        """Converts a raw input into 2D array."""
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
        self.number_of_rows = len(self.terrain_map)
        self.length_of_row = len(self.terrain_map[0])

    def count_islands(self) -> int:
        """Count islands using DPF algorithm."""

        def search_for_land(i: int, j: int) -> None:
            """Checks all neighbours for being a piece of land."""
            if (i, j) in visited_land or self._is_out_of_map(i, j) or not self._is_land(i, j):
                return None
            visited_land.add((i, j))
            search_for_land(i, j - 1)  # check right
            search_for_land(i, j + 1)  # check left
            search_for_land(i - 1, j)  # check up
            search_for_land(i + 1, j)  # check down
            search_for_land(i - 1, j - 1)  # check up left
            search_for_land(i - 1, j + 1)  # check up right
            search_for_land(i + 1, j + 1)  # check down right
            search_for_land(i + 1, j - 1)  # check down left

        visited_land = set()
        islands_count = 0
        for row in range(self.number_of_rows):
            for column in range(self.length_of_row):
                if self._is_land(row, column) and (row, column) not in visited_land:
                    search_for_land(row, column)
                    islands_count += 1
        return islands_count

    def _is_out_of_map(self, i: int, j: int) -> bool:
        """Checks whether index is out of array."""
        if i < 0 or i >= self.number_of_rows or j < 0 or j >= self.length_of_row:
            return True
        return False

    def _is_land(self, i: int, j: int) -> bool:
        """Checks if index has a LAND value (1)."""
        if self.terrain_map[i][j] == 1:
            return True
        return False


if __name__ == "__main__":
    raw_input = InputReader(file_path="test_input.txt").read_input()
    terrain_map = TerrainMapConverter(raw_input=raw_input).get_terrain_map()
    island_counter = IslandCounter(terrain_map=terrain_map)
    print(island_counter.count_islands())
