
def part_one(paper_map):
    total_rolls = 0
    for i, line in enumerate(paper_map):
        for j, char in enumerate(line):
            local_rolls = 0
            # print(f'looking into: {char} | {paper_map[i][j]}')
            if paper_map[i][j] == '@':
                for it in range(max(i-1, 0), min(i+2, len(line))):
                    for jt in range(max(j-1, 0), min(j+2, len(line))):
                        # print(f'POSITION ({it}, {jt}): {paper_map[it][jt]} ', end='| ')
                        
                        if it == i and j == jt:
                            continue
                        if paper_map[it][jt] == '@' or paper_map[it][jt] == 'X':
                            local_rolls += 1

                        if local_rolls >= 4:
                            break
                    if local_rolls >= 4:
                        break
                if local_rolls < 4:
                    total_rolls += 1
                    paper_map[i][j] = 'X'
            # print()
    return total_rolls

def remove_X(paper_map):
    for i, line in enumerate(paper_map):
        for j, char in enumerate(line):
            if char == 'X':
                paper_map[i][j] = '.'

def print_map(paper_map):
    for line in paper_map:
        for char in line:
            print(char, end=" ")
        print()

if __name__ == "__main__":
    with open("input_map_rolls.txt") as i_map_txt:
        papers_map_str = [[char for char in line.strip()] for line in i_map_txt]
        print(f'START PAPERS MAP')
        print_map(papers_map_str)

        total_rolls = 1
        total_rolls_count = 0
        while(total_rolls > 0):
            total_rolls = part_one(paper_map=papers_map_str)
            print(f'total rolls iteration: {total_rolls}')
            print_map(papers_map_str)
            remove_X(paper_map=papers_map_str)
            total_rolls_count += total_rolls
        # total_jolts = part_1(i_joltage_banks=i_joltage_txt)
        print()
        print_map(papers_map_str)
        print(f'TOTAL ROLLS: {total_rolls_count}')