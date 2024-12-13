from dataclasses import dataclass
from pathlib import Path
from typing import List, Self

puzzle = Path('puzzle').read_text()


@dataclass
class GameSet:
    blue: int = 0
    red: int = 0
    green: int = 0

    @classmethod
    def from_raw_data(cls, raw_data) -> Self:
        game_set = GameSet()
        cubes = raw_data.split(', ')
        for cube in cubes:
            number, color = cube.split()
            if color == 'blue':
                game_set.blue = int(number)
            elif color == 'red':
                game_set.red = int(number)
            else:
                game_set.green = int(number)
        return game_set

    def power(self) -> int:
        return self.red * self.blue * self.green


@dataclass
class Game:
    number: int
    game_sets: List[GameSet]

    def is_possible(self, max_blue: int, max_red: int, max_green: int) -> bool:
        for game_set in self.game_sets:
            if game_set.green > max_green or game_set.blue > max_blue or game_set.red > max_red:
                return False
        return True

    def find_minimum_cubes_set(self) -> GameSet:
        max_green = 0
        max_blue = 0
        max_red = 0
        for game_set in self.game_sets:
            if game_set.green > max_green:
                max_green = game_set.green
            if game_set.blue > max_blue:
                max_blue = game_set.blue
            if game_set.red > max_red:
                max_red = game_set.red
        return GameSet(blue=max_blue, green=max_green, red=max_red)


def get_game_data_from_line(line: str, line_index: int) -> Game:
    data = line.split(': ')[1].split(';')
    game = Game(number=line_index, game_sets=[])
    for game_set in data:
        game.game_sets.append(GameSet.from_raw_data(game_set))
    return game


sum_of_ids = 0
sum_of_powers = 0
for i, line in enumerate(puzzle.splitlines()):
    game = get_game_data_from_line(line, i + 1)
    if game.is_possible(max_green=13, max_blue=14, max_red=12):
        sum_of_ids += game.number

    power = game.find_minimum_cubes_set().power()
    sum_of_powers += power

print(sum_of_ids)
print(sum_of_powers)
