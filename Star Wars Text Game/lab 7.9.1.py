# Type your code here
user_input = file1

with open("user_input", "r") as user_input_read:
    user_input_read_lines = user_input_read.readlines()
    print(user_input_read_lines)