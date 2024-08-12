# Check the comments on ctflearn... Apparently there are some typo's in the assignment here.
def symbolic_decimal(ch):
    given_str = "!@#$%^&*()"
    given_repl_str = "1234567890"
    found_index = given_str.find(ch)
    if found_index >= 0:
        return given_repl_str[found_index]
    else:
        return False

def symbolic_num(numstr):
    result = ""
    for i in range(len(numstr)):
        result += symbolic_decimal(numstr[i])
    return int(result)


input_str = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"
split_input_str = input_str.split(',')

result = ""
for inp in split_input_str:
    result += chr(symbolic_num(inp))
print(result)
