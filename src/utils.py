
import os, sys
from pathlib import Path

project_dir = Path(__file__).parent.parent.absolute()
aocd_dir = project_dir / "aocd-data"

os.environ["AOCD_DIR"] = str(aocd_dir)

from aocd import get_data, submit
from aocd.get import get_day_and_year

import logging

def lines(**kwargs):
    return get_data(**kwargs).split("\n")

def text(**kwargs):
    return get_data(**kwargs).split("\n")

def filename(**kwargs):
    if "day" not in kwargs or "year" not in kwargs:
        logging.error("'day' and 'year' must be provided for file input")
        sys.exit(1)
    get_data(**kwargs)
    filename = kwargs["year"] + "_" + kwargs["day"] + "_*.txt"
    rg = list(aocd_dir.rglob(filename))
    if not len(rg):
        logging.error("Make sure your 'day' and 'year' are valid values")
        sys.exit(1)
    return str(rg[0])

def file(**kwargs):
    return open(filename(**kwargs))

def part_wrapper(part, datafn):
    def outer_decorator(*vargs, **kwargs):
        def inner_decorator(fn):
            def wrapped():
                fn_name = f"{fn.__module__}.{fn.__qualname__}"
                logging.info(f"Running {fn_name}...")
                result = fn(datafn(**kwargs))

                if result is None:
                    logging.error(f"The function {fn_name} does not return any data. Be sure to include `return <your_answer>` at the end of your code")
                    sys.exit(1)
                else:
                    print(f"The solution to Part {part} is {result}")
                #else:
                #    submit(answer=result, part=part)
            setattr(wrapped, "part", part)
            return wrapped
        return inner_decorator
    return outer_decorator

answer_part_a = part_wrapper("a", lines)
answer_part_b = part_wrapper("b", lines)

answer_part_a_text = part_wrapper("a", text)
answer_part_b_text = part_wrapper("b", text)

answer_part_a_filename = part_wrapper("a", filename)
answer_part_b_filename = part_wrapper("b", filename)

answer_part_a_file = part_wrapper("a", file)
answer_part_b_file = part_wrapper("b", file)