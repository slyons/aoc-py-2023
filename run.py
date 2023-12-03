from pathlib import Path
import importlib, sys
import logging

def run():
    logging.basicConfig()
    proj_dir = Path(__file__).parent.absolute()
    sys.path.insert(0, str(proj_dir / "src"))

    ###
    # Find the most recent solution
    ###
    solutions_dir = proj_dir / "src" / "solutions"
    solution_modules = list(map(lambda x: x.name.split(".")[0], filter(lambda x: "template" not in str(x), solutions_dir.rglob("*.py"))))
    solution_modules.sort(reverse=True)

    ###
    # Filter based on arguments
    ###
    if len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]
        print(f"Running for year {year} day {day}")
        filter_str = f"{year}_{day:0>2}"
        solution_modules = list(filter(lambda x: x.startswith(filter_str), solution_modules))

    ###
    # Load the module and search for solution functions
    ###
    next_fns = None
    for module in solution_modules:
        mod = __import__(f"solutions.{module}", fromlist=[module])
        fn_defns = list(map(lambda x: getattr(mod, x), filter(lambda x: hasattr(getattr(mod, x), "part"), dir(mod))))
        if len(fn_defns):
            next_fns = fn_defns
            break
    else:
        logging.error("Could not find any functions marked `part_a` or `part_b`. Make sure your file is named `year_day.py`, i.e 2023_01.py")
        sys.exit(1)
    
    next_fns.sort()
    for fn in next_fns:
        fn_name = f"{fn.__module__}.{fn.__qualname__}"
        logging.info(f"Running {fn_name}...")
        fn()


if __name__ == "__main__":
    run()
