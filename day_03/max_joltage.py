

if __name__ == "__main__":
    with open("input_joltage.txt") as i_joltage_txt:
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
        print()
        print(f'TOTAL JOLTS: {total_jolts}')