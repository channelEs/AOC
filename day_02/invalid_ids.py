def ids_iteration(first_part, min_range, end_range, invalid_ids=[]):
    if int(first_part + first_part) > end_range:
        print(f'END WITH: {first_part}')
        return invalid_ids
    
    if int(first_part + first_part) >= min_range:
        print(f'ADD ID {first_part}{first_part}', end=' , ')
        invalid_ids.append(first_part + first_part)
    new_first_part = str(int(first_part) + 1)
    return ids_iteration(new_first_part, min_range, end_range, invalid_ids=invalid_ids)

def check_current_id(current_id, min_range, end_range, invalid_ids=[]):
    first_part = current_id[:int(len(current_id)/2)] 
    second_part = current_id[int(len(current_id)/2):] 
    print(f'checking from FIRST PART: {first_part} | SECOND PART: {second_part}')
    if len(current_id)%2 != 0:
        # first_part = second_part[int(len(second_part))-1] + first_part
        if len(first_part) == 0:
            first_part = '0'
        # first_part = str(int('1'+first_part) - int(first_part))
        # print(f'Modified first part: {first_part}')
        current_id = str(int('1'+current_id) - int(current_id))
        first_part = current_id[:int(len(current_id)/2)] 
        # second_part = current_id[int(len(current_id)/2):] 
        print(f'Modified current_id: {current_id}')
    
    return ids_iteration(first_part, min_range, end_range, invalid_ids=invalid_ids)      

def second_part(checking_id, invalid_ids=[]):
    divide_iterator = 2
    
    can_be_invalid = True
    while(can_be_invalid):
        if len(checking_id)%divide_iterator == 0:
            i_0 = 0
            i_1 = int(len(checking_id)/divide_iterator)
            part_0 = checking_id[i_0:i_1]
            for i in range(1, divide_iterator):
                i_0 = int(i*len(checking_id)/divide_iterator)
                i_1 = int((i+1)*len(checking_id)/divide_iterator)
                part_i = checking_id[i_0:i_1]
                
                if part_0 != part_i:
                    can_be_invalid = False
                    break
            if can_be_invalid:
                # print(f'{checking_id} IS INVALID', end=' , ')
                invalid_ids.append(checking_id)
                break
            else:
                can_be_invalid = True
        divide_iterator += 1
        if divide_iterator > len(checking_id):
            break
    return invalid_ids

if __name__ == "__main__":
    with open("input.txt") as input_txt:
        ids_ranges = input_txt.readlines()[0].split(',')
        print(f'READED: {ids_ranges}')
        final_sum = 0
        for id_range in ids_ranges:
            id_start = id_range.split('-')[0].strip()
            id_end = id_range.split('-')[1]
            print()
            print(f'RANGE: [{id_start},{id_end}]')
            
            invalid_ids = []
            # invalid_ids = check_current_id(id_start, int(id_start), int(id_end), invalid_ids=invalid_ids)
            for current_id in range(int(id_start), int(id_end)+1):
                invalid_ids = second_part(str(current_id), invalid_ids=invalid_ids)
            # invalid_ids = second_part(id_start, invalid_ids=invalid_ids)
            print(f'INVALID IDS: {invalid_ids}')

            for invalid_id in invalid_ids:
                final_sum += int(invalid_id)
            print(f'FINAL SUM: {final_sum}')