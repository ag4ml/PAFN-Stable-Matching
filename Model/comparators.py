def string_cmp_fn(multiplier):
    def string_compare(advisor_string, advisee_string):
        score = 0
        advisor_array_str = advisor_string.split(",")
        advisee_array_str = advisee_string.split(",")
        #sanitization
        for i in range(0, len(advisor_array_str)):
            advisor_array_str[i] = advisor_array_str[i].strip().lower()
        for i in range(0, len(advisee_array_str)):
            advisee_array_str[i] = advisee_array_str[i].strip().lower()
        #tight comparison
        for string_val in advisee_array_str:
            if string_val in advisor_array_str:
                score+=1
        #loose comparison - advisee to advisor then advisor to advisee
        compare_str = advisor_array_str.join(" ")
        for string_val in advisee_array_str:
            if string_val in compare_str:
                score +=1
        compare_str = advisee_array_str.join(" ")
        for string_val in advisor_array_str:
            if string_val in compare_str:
                score+=1
        return score*multiplier
    return string_compare

def num_cmp_fn(multiplier):
    def num_compare(advisor_num, advisee_num):
        abs_diff = abs(advisor_num-advisee_num)
        avg = (advisor_num+advisee_num)/2
        score = 2 - (abs_diff/avg)
        return score * multiplier
    return num_compare
