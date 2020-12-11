import copy

adjacent = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)]


def iterate(seats: dict):
    new_seats = copy.deepcopy(seats)
    for (x, y), v in seats.items():
        if v == ".":
            continue
        occupied_adjacent = 0
        for dx, dy in adjacent:
            nx, ny = x + dx, y + dy
            if (nx, ny) in seats and seats[nx, ny] == "#":
                occupied_adjacent += 1
        if v == "L" and not occupied_adjacent:
            new_seats[x, y] = "#"
        elif v == "#" and occupied_adjacent >= 4:
            new_seats[x, y] = "L"
    return new_seats


def part_1(seats: dict):
    new_seats = iterate(seats)
    while seats != new_seats:
        seats = new_seats
        new_seats = iterate(seats)

    return len([v for v in seats.values() if v == "#"])


def part_2(seats: dict):
    pass


if __name__ == "__main__":
    with open("data.txt") as f:
        seats = f.read()
    seats = seats.split("\n")
    seats = {(i, j): s for i in range(len(seats)) for j, s in enumerate(seats[i])}

    print(part_1(seats))
    print(part_2(seats))
