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

    def count_islands(self) -> int:
        """Count islands using DPF algorithm."""

        number_of_rows = len(self.terrain_map)
        length_of_row = len(self.terrain_map[0])

        def is_out_of_map(i: int, j: int) -> bool:
            """Checks whether index is out of array."""
            if i < 0 or i >= number_of_rows or j < 0 or j >= length_of_row:
                return True
            return False

        def is_land(i: int, j: int) -> bool:
            """Checks if index has a LAND value (1)."""
            if self.terrain_map[i][j] == 1:
                return True
            return False

        def search_for_land(i: int, j: int) -> None:
            """Checks all neighbours for being a piece of land."""
            if (i, j) in visited_land or is_out_of_map(i, j) or not is_land(i, j):
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
        for row in range(number_of_rows):
            for column in range(length_of_row):
                if is_land(row, column) and (row, column) not in visited_land:
                    search_for_land(row, column)
                    islands_count += 1
        return islands_count


if __name__ == "__main__":
    raw_input = InputReader(file_path="test_input.txt").read_input()
    terrain_map = TerrainMapConverter(raw_input=raw_input).get_terrain_map()
    island_counter = IslandCounter(terrain_map=terrain_map)
    print(island_counter.count_islands())
