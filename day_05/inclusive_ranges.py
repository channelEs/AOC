def integrate_new_range(ranges: list, min_value, max_value):
    i_range_min = -1
    min_in_range = False
    i_range_max = -1
    max_in_range = False
    for i, range_i in enumerate(ranges):
        if min_value < range_i[0]:
            i_range_min = i
            break
        if min_value >= range_i[0] and min_value <= range_i[1]:
            i_range_min = i
            min_in_range = True
            break
        
    for i, range_i in enumerate(ranges):
        if max_value < range_i[0]:
            i_range_max = i
            break
        if max_value >= range_i[0] and max_value <= range_i[1]:
            i_range_max = i
            max_in_range = True
            break

    new_min = min_value
    new_max = max_value

    print(f'CURRENT RANGES: {ranges} | ({min_value}, {max_value}) -- [{i_range_min}, {i_range_max}]')
    if i_range_min == i_range_max and not min_in_range and not max_in_range:
        ranges.insert(i_range_min, [new_min, new_max])
        return
    
    if i_range_max == -1:
        i_range_max = len(ranges)-1

    if min_in_range:
        ranges[i_range_min][0] = ranges[i_range_min][0]
    else:
        ranges[i_range_min][0] = new_min
    
    if max_in_range:
        ranges[i_range_min][1] = ranges[i_range_max][1]
    else:
        ranges[i_range_min][1] = new_max

    for pop_i in range(i_range_min+1, i_range_min+1 + (i_range_max-i_range_min)):
        print(f'POPING i: {pop_i}')
        ranges.pop(i_range_min+1)

def construct_ranges(ranges_txt):
    final_ranges = []
    for range_txt in ranges_txt:
        min = range_txt.split('-')[0]
        max = range_txt.split('-')[1]
        integrate_new_range(ranges=final_ranges, min_value=int(min), max_value=int(max))
    print(f'FINAL RANGES: {final_ranges}')
    return final_ranges

def id_in_ranges(ranges, value):
    is_in = False
    for range in ranges:
        if value <= range[1] and value >= range[0]:
            is_in = True
            break
    return is_in

def count_part_two(ranges):
    total_count = 0
    for range_i in ranges:
        total_count += range_i[1] - range_i[0] + 1
    return total_count

if __name__ == "__main__":
    with open("input_ranges_IDs.txt") as i_inclusive:
        txt_lines = i_inclusive.readlines()
        i = 0
        ranges_txt = []
        for ranges_line in txt_lines:
            i += 1
            if len(ranges_line) == 1:
                break
            ranges_txt.append(ranges_line.strip())
        # ids = []
        # for id_line in range(i, len(txt_lines)):
        #     ids.append(int(txt_lines[id_line].strip()))

        print(f'RANGES: {ranges_txt}')
        # print(f'IDS: {ids}')

        ranges = construct_ranges(ranges_txt=ranges_txt)
        # total_id_count = 0
        # for id in ids:
        #     if id_in_ranges(ranges=ranges, value=id):
        #         total_id_count += 1
        # print()
        # print(f'TOTAL INCLUSIVE: {total_id_count}')

        total_FRESH_INCLUSIVE = count_part_two(ranges)
        print(f'TOTAL INCLUSIVE: {total_FRESH_INCLUSIVE}')