def arithmetic_arranger(lst,show_answer = False):
    # Setting Parameters and if statement properly
    max_len = 0
    count = 0
    for i in lst:
        j = i.split()
        for i in j:
            if j[0].isnumeric() is False or j[2].isnumeric() is False: 
                count += 1    
            if len(i) > max_len:
                max_len = len(i)
    # Error Conditions
    if len(lst) > 5: 
        return("Error: Too many problems.")
    elif max_len > 4: 
        return("Error: Numbers cannot be more than four digits.")
    elif count > 0: 
        return("Error: Numbers must only contain digits.")
    else:
        first_operands = ""
        for i in range(len(lst)):
            seperate = lst[i].split()
            max_length = 0
            for values in seperate:
                if len(values) > max_length:
                    max_length = len(values)
                    adjusted_max_length = max_length + 2
            s = ""
            white_space = "    " # Four spaces required between each of the lists
            for spaces in range(adjusted_max_length - len(seperate[0])):
                s += " "
            first_operands += (s + seperate[0] + white_space)
        first_operands = first_operands.rstrip()
        second_operands = ""
        for i in lst:
            # To get max length
            seperate = i.split()
            max_length = 0
            for values in seperate:
                if len(values) > max_length:
                    max_length = len(values)
            # To get the operator signs --> + or - and arrange properly according to the question
            mid = i.split()[1]
            y = max_length - len(i.split()[2]) + 1
            num_of_spaces = y * " " # Number of spaces between sign and operands
            second_operands += (mid + num_of_spaces + i.split()[2] + white_space)
        second_operands = second_operands.rstrip()
        # To place the seperator --> ----- for each
        dash_seperator = ""
        for i in lst:
            seperate = i.split()
            max_length = 0
            for values in seperate:
                if len(values) > max_length:
                    max_length = len(values)
                    adjusted_max_length = max_length + 2
            dash = "-"
            num_of_dashes = adjusted_max_length * dash
            dash_seperator += num_of_dashes + white_space
        dash_seperator = dash_seperator.rstrip()
        # Calculating the values
        answers = ""
        for i in lst:
            seperate = i.split()
            max_length = 0
            for values in seperate:
                if len(values) > max_length:
                    max_length = len(values)
            if seperate[1] == "+":
                ans = str(int(seperate[0]) + int(seperate[2]))
            elif seperate[1] == "-":
                ans = str(int(seperate[0]) - int(seperate[2]))
            else:
                return "Error: Operator must be '+' or '-'."
            # Formatting the answers
            num_of_spaces = max_length - len(ans) + 2
            dash = " "
            # Show/Hide Anser
            if show_answer is True:
                answers += num_of_spaces * dash + ans + white_space
                formated_answers = first_operands + "\n" + second_operands + "\n" + dash_seperator + "\n" + answers.rstrip()
            else:
                formated_answers = first_operands + "\n" + second_operands + "\n" + dash_seperator
    return formated_answers
x = ["11 + 4","3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
print(arithmetic_arranger(x))