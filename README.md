# Advent of Code 2023

## Python/Git setup

These steps should be done once

1. Sign up for a [Github account](https://github.com/signup?source=header-home)
2. Install [Anaconda](https://www.anaconda.com/download)
3. Install [VSCode](https://code.visualstudio.com/)
4. This will install a new shortcut: `Anaconda Console`. Running this will let you run Python code.
5. Open this new console and run `conda install -c anaconda git`. This will install git, a version control tool.
6. [Fork](https://github.com/slyons/aoc-py-2023/fork) my code. This will make your own copy in your account. You will push your changes to this copy so that I can see them.
7. Inside your `Anaconda` console, go to a directory where you want to keep your code
8. Run `git clone https://github.com/<your_github_username>/aoc-py-2023`
9. `cd aoc-py-2023`
10. `pip install -r requirements.txt`
11. Sign up for an account at [Advent of Code](https://adventofcode.com/) using **Chrome**
12. Click on `Leaderboard` and input the team ID I give you
13. Create a directory named `aocd-data` in your project directory (same folder as `src` lives in)
14. Follow [these instructions](https://github.com/wimglenn/advent-of-code/issues/1) to get your Session ID (a long string of letters and numbers). Create a new file named `token` in `aocd-data` and paste the Session ID into it.
15. `aocd 2018 1` should print out a bunch of lines

## Puzzles

The Advent of Code (AoC from here on out) is a yearly coding challenge that uses Christmas-themed challenges to help coders push their skills or acquire new ones.

Each puzzle has three parts:

1. The input (more on this in a minute)
2. Puzzle part A
3. Puzzle part B

With each challenge, you'll take the input, come up with an answer for Part A which will then unlock Part B. Part B will use the same input, but produce a different answer.

## Test framework

I've put together a small framework to help you focus on solving the problems. You'll create solution files in `src/solutions` with the naming pattern of `<year>_<day>.py`, i.e `2023_01.py`. This name pattern is important as it how the framework finds your solutions.

Inside each solution file, you'll need to provide two functions. Functions are re-usable pieces of code. They'll be used to provide your two solutions (two functions per file). You will `return` your answer for each part, and your answer will automatically be submitted for you. You'll just need to go to the AoC website to read the challenge.

I've created a series of utilities that will automatically fetch the input for you in a variety of ways. You'll start with the easy one, then you can progress to the more challenging version. 

### The Solutions

So, if challenge Part A was to count the number of lines in the input, you would write:

```python
@answer_part_a(year=2023, day=1)
def part_1(lines):
    return len(lines)
```

Let's dissect this example piece by piece.

#### Input data

```python
@answer_part_a(year=2023, day=1)
```

This line says that this answer is for 2023 day 1, part A. The `answer_part_a` or (`answer_part_b`) is one of a few shortcuts that will change the way the data is provided to your function. In this case, it's provided as an array (`list`) of lines of input. For more advanced versions (like working with file paths directly) message me and I'll tell you what's available.

`lines` will look like this:

```python
[
    "2477",
    "1999",
    "4809",
    ...
]
```

#### Solution function

```python
@def part_1(lines):
```

This is your function, it can be named whatever you want.

#### Returning the answer

```python
    return len(lines)
```

This is my answer for Challenge Part A (the number of lines in the input). Whatever you return will be submitted as your answer. You can also submit your answer in the browser if something goes wrong. You'll be told if your answer is too high or too low.

#### Debugging

You can use things like `print` to print the input, or during your calculations to debug. If you want a more advanced debugger message me and I'll tell you about it.

### Running your solutions

In the root of the project, run `python run.py`. It should run your most recent solution and submit the answer. 

## Your workflow

Your workflow should be these steps:

1. Read the challenge
2. Read it again
3. Create a solution file (`2023_X.py`)
4. Read the challenge again
5. Create your solutions
6. Run your solutions
7. Save your work (`git add src\solutions\2023_X.py`, `git commit`, see below for more specific commands)

### Saving your work

This project is based on Git, which is a distributed version control system. For our purposes, it should be easy enough to use. 

The steps that you should follow are:

1. `add` new/changed files
2. `commit` your changes
3. `push` to sync

When you want to check the status of your project according to Git, you run `git status`

#### Adding new files

When you've created a new file, `git status` will show:

```
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	README.md
```

In order for Git to pay attention to a file, you have to `add` it. So run `git add <path\to\file>`. Continue on to the Commit phase.

#### Changing existing files

Surprisingly, it's the same as adding new files, except that you need to add it when you're done making changes. `git status` will show something like this:

```
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   src/utils.py
```

#### Committing changes

Committing is Git's way of tracking changes. It creates a snapshot of your repo at a certain point in time. Once you've `add`-ed your files, you run:

`git commit -m "Your commit message"`

The `"Your commit message"` should be something that describes your changes

#### Pushing changes

A `push` in Git terms synchronizes a remote repo with your local changes. You should do this regularly so that I can take a look at your code and critique it.

When you run `git push` you should see something like:

```
✓ Pushed commits to https://github.com/<your_github_username>/aoc-py-2023.git
```

If you see this and you've made changes to your files:

```
❯ git push
Everything up-to-date
```

That means you didn't `add`/`commit` properly. Try it again, check `git status`.

#### Full workflow example

While editing this README I did the following once I was done with my work:

```shell
❯ git add README.md

❯ git commit -m "Updating README with instructions"
[main 2f8aec7] Updating README with instructions
 1 file changed, 177 insertions(+)
 create mode 100644 README.md

❯ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 10 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 2.99 KiB | 2.99 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/slyons/aoc-py-2023.git
   9a4f734..2f8aec7  main -> main
```