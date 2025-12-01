

if __name__ == "__main__":

    current_position = 50
    zero_counter = 0

    with open("input_rotations.txt") as input_txt_rotations:
        for rotation_lines_txt in input_txt_rotations:
            rotation_direction = rotation_lines_txt[0]
            rotation_value = int(rotation_lines_txt[1:].strip())

            print(f"MOVING TO {rotation_direction} WITH VALUE {rotation_value} [{current_position}]", end=" | ")
            if rotation_lines_txt[0] == 'R':
                current_position += rotation_value
                while current_position > 99:
                    current_position -= 100
                    print()
                    print(f"ZERO POSITION")
                    zero_counter += 1

            else:
                start_from_0 = False
                if current_position == 0:
                    start_from_0 = True

                current_position -= rotation_value
                while current_position < 0:
                    current_position += 100
                    if not start_from_0:
                        print()
                        print(f"ZERO POSITION")
                        zero_counter += 1
                    else:
                        start_from_0 = False

                if current_position == 0:
                    print()
                    print(f"ZERO POSITION")
                    zero_counter += 1

    print()
    print(f'ZERO COUNTER: {zero_counter}')