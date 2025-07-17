# Linux CD/PWD Simulator

This project simulates the behavior of basic Linux commands `cd` and `pwd` using Python 3.12.  
It was originally developed as a solution to a recruitment challenge.

## Features

- Simulates navigating the file system using `cd` and `pwd`
- Handles absolute and relative paths
- Ignores redundant path components like `.` or empty segments
- Maintains internal state as a list (stack-like behavior)

## Input Format

- First line: number of commands `t` (1 ≤ t ≤ 50)
- Next `t` lines: commands like `cd /path`, `cd ..`, or `pwd`

## Sample Input

```bash
> 4
> cd /home/user
> cd ..
> pwd
> cd tmp
```

## Sample Output

```bash
> /home
> /home/tmp
```

## Running the Code

You can run the script and provide input via standard input:

```bash
python3 main.py
```

or using a file:

```bash
cat input.txt | python3 main.py
```

