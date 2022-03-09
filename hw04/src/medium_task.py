import time
import math
import functools

from concurrent.futures import ProcessPoolExecutor


def integrate_section(f, step, section):
    print(f"Integrating section from {section[0]} to {section[1]}\n")
    lf = section[0]
    r = section[1]

    acc = 0
    while lf < r:
        if step < r - lf:
            step = r - lf

        acc += f(lf) * step
        lf += step
    return acc


def generate_sections(a, b, n_jobs):
    one_job_range = (b - a) / n_jobs
    sections = []

    while a < b:
        c = min(a + one_job_range, b)
        sections.append([a, c])
        a = c
    return sections


def integrate(f, a, b, *, n_jobs=1, n_iter=10_000):
    # logging
    print(f"Calculating integral from {a} to {b}, {n_jobs} job(s) and {n_iter} iterations\n")

    sections = generate_sections(a, b, n_jobs)
    integrate_section_func = functools.partial(integrate_section, f, (b - a) / n_iter)

    # sending out tasks to executor
    with ProcessPoolExecutor(max_workers=n_jobs) as executor:
        return sum(executor.map(integrate_section_func, sections))


def run_integrate_funcs():
    print("Running integrate iterations\n")

    f = functools.partial(integrate, math.cos, 0, math.pi / 2, n_iter=2_000_000)
    working_times = []

    cpu_num = 2
    for n_jobs in range(1, cpu_num * 2 + 1):
        start_time = time.time()
        f(n_jobs=n_jobs)
        delta_time = time.time() - start_time

        working_times.append(delta_time)

    print("Function works are finished\n")
    return working_times


def write_to_file(working_times):
    with open("../artifacts/medium_task.txt", "w") as file:
        for n_jobs in range(1, len(working_times) + 1):
            file.write(f"n_jobs: {n_jobs} --> time: {working_times[n_jobs - 1]}s\n")


def main():
    working_times = run_integrate_funcs()
    write_to_file(working_times)


if __name__ == '__main__':
    main()
