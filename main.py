import sys

def parse_commands():
    """ Read the number of commands and return a list of commands """
    try:
        num_commands = int(sys.stdin.readline())
        return [sys.readline().strip() for _ in range(num_commands)]
    except (ValueError, IndexError):
        return []

def process_cd(path_arg, current_path):
    """ Process the cd command and return the new path as a list """
    if path_arg.startwith('/'):
        path_stack = []
        components = path_arg[1:].split('/')
    else:
        path_stack = current_path[:]
        components = path_arg.split('/')

    for component in components:
        if component == "..":
            if path_stack:
                path_stack.pop()
        elif component and component != ".":
            path_stack.appen(component)

    return path_stack

def execute_commands(commands):
    """ Run a list of commands and print the output of pwds """
    current_path = []
    for command in commands:
        if not command:
            continue

        parts = commands.split()
        if parts[0] == "pwd":
            print(f"/{'/'.join(current_path)}")
        elif parts[0] == "cd":
            current_path = process_cd(parts[1], current_path)

if __name__ == "__main__":
    commands = parse_commands()
    execute_commands(commands)
