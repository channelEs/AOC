def part_1(i_joltage_banks: list = []):
    total_jolts = 0
    for battery in i_joltage_txt:
        print(f'BATTERY JOLTAGE: {battery}')

        max_0 = 0
        max_1 = 0

        for i, joltage_value in enumerate(battery.strip()):
            print(f'position {i} value {joltage_value}', end=' | ')
            joltage_value = int(joltage_value)
            if joltage_value > max_0 and i < len(battery.strip()) - 1:
                max_0 = joltage_value
                max_1 = 0
            elif joltage_value > max_1:
                max_1 = joltage_value
        bank_jolts = max_0*10 + max_1
        print()
        print(f'bank jolts: {bank_jolts}')
        total_jolts += bank_jolts
    return total_jolts

def part_2(N: int = 2, i_joltage_banks: list = []):
    total_jolts = 0
    for battery in i_joltage_txt:
        print()
        print(f'battery: {battery.strip()} | length: {len(battery.strip())} | N: {N}')
        bank_result = ['0' for _ in range(N)]
        for i, joltage_value in enumerate(battery.strip()):
            i_position = 0
            if len(battery.strip()) - i < N:
                i_position = N - (len(battery.strip()) - i)
            setted = False
            while not setted and i_position < N:
                print(f'i = {i_position} | joltage = {joltage_value} bank_result: {bank_result}')
                if int(joltage_value) > int(bank_result[i_position]) and len(battery.strip()) - i >= N - i_position:
                    bank_result[i_position] = joltage_value
                    bank_result[i_position+1:] = ['0' for _ in range(N - (i_position+1))]
                    setted = True
                i_position += 1
        print(f'bank_result: {bank_result}')
        total_jolts_bank_str = ''
        for joltage in bank_result:
            total_jolts_bank_str += joltage
            # print(f'total: {total_jolts_bank_str}')
        total_jolts += int(total_jolts_bank_str)
    return total_jolts



if __name__ == "__main__":
    with open("input_joltage_t.txt") as i_joltage_txt:
        # total_jolts = part_1(i_joltage_banks=i_joltage_txt)
        total_jolts = part_2(N=12, i_joltage_banks=i_joltage_txt)
        print()
        print(f'TOTAL JOLTS: {total_jolts}')
        