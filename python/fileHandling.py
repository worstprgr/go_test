from pathlib import Path

# init
string = [f'Test{x} ' for x in range(10)]

string_add = [f'_add{x} ' for x in range(2)]

fileName = 'test.txt'


# write file helper
def helper(inp, mode):
    with open(fileName, mode, encoding='utf8') as f:
        f.writelines(inp)


# create file
Path(fileName).touch(exist_ok=True)

# write: w
helper(string, 'w')

# write: a
helper(string_add, 'a')
