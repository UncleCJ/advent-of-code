# Advent of code Year 2020 Day 11 solution
# Author = BNAndras
# Date = December 2020

from collections import namedtuple
from copy import deepcopy


def initialize_seating_chart(data):
    initial_state = dict()

    for row_index, row_value in enumerate(data):
        for column_index, column_value in enumerate(row_value):
            initial_state[Position(column_index, row_index)] = column_value

    return initial_state


def cycle_seating_chart_until_stable(current_state_of_seating_chart):
    current_state_of_seating_chart = deepcopy(current_state_of_seating_chart)
    next_state_of_seating_chart = (
        run_through_seating_chart(current_state_of_seating_chart)
    )

    while next_state_of_seating_chart != current_state_of_seating_chart:
        current_state_of_seating_chart = next_state_of_seating_chart
        next_state_of_seating_chart = (
            run_through_seating_chart(current_state_of_seating_chart)
        )

    return current_state_of_seating_chart


def run_through_seating_chart(incoming_state_of_chart):
    global part_two_flag

    copy_of_current_state = deepcopy(incoming_state_of_chart)
    threshold_for_occupied_neighbors = 4 if not part_two_flag else 5

    for position_in_current_state in copy_of_current_state:
        if position_in_current_state == symbol_for_unavailable_seat:
            continue
        count_of_occupied_neighbors = (
            count_available_neighboring_seats(incoming_state_of_chart, position_in_current_state)
        )
        if (copy_of_current_state[position_in_current_state] == symbol_for_available_seat
                and not count_of_occupied_neighbors):
            copy_of_current_state[position_in_current_state] = symbol_for_occupied_seat
        elif (copy_of_current_state[position_in_current_state] == symbol_for_occupied_seat
              and count_of_occupied_neighbors >= threshold_for_occupied_neighbors):
            copy_of_current_state[position_in_current_state] = symbol_for_available_seat

    return copy_of_current_state


def count_available_neighboring_seats(copy_of_current_state, target_seat_position):
    global part_two_flag

    relative_offsets_for_neighbors = [
        Position(X=0, Y=-1), Position(X=-1, Y=-1), Position(X=-1, Y=0), Position(X=-1, Y=1),
        Position(X=0, Y=1), Position(X=1, Y=1), Position(X=1, Y=0), Position(X=1, Y=-1),
    ]

    count_of_occupied_neighbors = 0
    for relative_offset in relative_offsets_for_neighbors:
        current_neighbor_position = Position(
            target_seat_position.X + relative_offset.X, target_seat_position.Y + relative_offset.Y
        )
        if part_two_flag:
            current_ring_of_neighboring_seats = 1
            while copy_of_current_state.get(current_neighbor_position) == symbol_for_unavailable_seat:
                current_neighbor_position = copy_of_current_state.get(
                    Position(
                        current_neighbor_position.X + (relative_offset.X * current_ring_of_neighboring_seats),
                        current_neighbor_position.Y + (relative_offset.Y * current_ring_of_neighboring_seats),
                    )
                )
                current_ring_of_neighboring_seats += 1
            if copy_of_current_state.get(current_neighbor_position) == symbol_for_occupied_seat:
                count_of_occupied_neighbors += 1
        elif copy_of_current_state.get(current_neighbor_position, symbol_for_available_seat) == symbol_for_occupied_seat:
            count_of_occupied_neighbors += 1

    return count_of_occupied_neighbors


with open((__file__.rstrip("puzzle.py") + "input.txt"), 'r') as input_file:
    inp = input_file.read()
    lines = inp.splitlines()

symbol_for_unavailable_seat = "."
symbol_for_available_seat = "L"
symbol_for_occupied_seat = "#"
Position = namedtuple("Position", "X Y")

initial_state_of_seating_chart = initialize_seating_chart(lines)

part_two_flag = False
stable_seating_chart_for_part1 = cycle_seating_chart_until_stable(initial_state_of_seating_chart)
count_of_occupied_seats_for_part1 = sum(
    1 for seat_position in stable_seating_chart_for_part1.values() if seat_position == symbol_for_occupied_seat
)
print("Part One : {}".format(count_of_occupied_seats_for_part1))

part_two_flag = not part_two_flag
stable_seating_chart_for_part2 = cycle_seating_chart_until_stable(initial_state_of_seating_chart)
count_of_occupied_seats_for_part2 = sum(
    1 for seat_position in stable_seating_chart_for_part2.values() if seat_position == symbol_for_occupied_seat
)
print("Part Two : {}".format(count_of_occupied_seats_for_part2))
