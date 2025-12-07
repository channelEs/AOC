

if __name__ == "__main__":
    with open("input_math.txt") as i_inclusive:
        txt_lines = i_inclusive.readlines()

        i_operators = []
        operator_line = txt_lines[len(txt_lines)-1]
        i_operator_indx = []
        is_product_operator = []
        for i, char_in_line in enumerate(operator_line):
            if char_in_line == '+' or char_in_line == '*':
                i_operator_indx.append(i)
                if char_in_line == '+':
                    is_product_operator.append(False)
                else:
                    is_product_operator.append(True)
        txt_lines.pop()

        print(txt_lines)
        print(i_operator_indx)
        print(is_product_operator)
        # print(f'THIS WORKS? str 1234 -> {int(" 1234  ")}')
        total_value = 0
        for i, start_i in enumerate(i_operator_indx):
            total_column_value = 0
            for line in txt_lines:
                if i == len(i_operator_indx)-1:
                    end_i = len(line)-1
                else:
                    end_i = i_operator_indx[i+1]
                int_value = int(line[start_i:end_i])
                print(f'VALUE READED {int_value}', end=" ")
                if is_product_operator[i]:
                    if total_column_value == 0:
                        total_column_value = int_value
                    else:
                        total_column_value = total_column_value * int_value
                else:
                    total_column_value += int_value
            print(f'COLUMN VALUE {total_column_value}')
            total_value += total_column_value
            
        print(f'TOTAL VALUE: {total_value}')
        