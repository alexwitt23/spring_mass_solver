#!/usr/bin/env python3

import argparse
import sys
from typing import List

import numpy as np

_GRAVITY = 9.80665  # m / s^2


def print_system(
    num_springs: int, num_masses: int, fix_top: bool, fix_bottom: bool
) -> None:
    system = ""
    spring = "  |  \n  /  \n  \\\n  |  \n"
    mass = "  O  \n"

    if fix_top:
        system += "/////\n____\n"
        system += spring
        num_springs -= 1

    for idx in range(num_masses):
        if idx:
            system += spring
            num_springs -= 1
        system += mass

    if fix_bottom:
        if not num_springs:
            print(
                "The system you've defined is improper. You have supplied "
                f"{num_springs} springs, but more are needed to complete the system. "
            )
            sys.exit(1)

        system += spring
        system += " ____\n/////\n"

    print("Your system:")
    print(system)


def return_difference_matrix(rows: int, cols: int, k: int) -> np.ndarray:
    eye = np.eye(rows, cols, k=1 + k)
    eye -= np.eye(rows, cols, k=k)
    return np.matrix(eye)


def return_force_vector(masses: List[float]) -> np.ndarray:
    return np.matrix([_GRAVITY * mass for mass in masses]).transpose()


def return_spring_constant_matrix(spring_constants: List[float]) -> np.ndarray:
    mat = np.zeros((len(spring_constants), len(spring_constants)), int)
    np.fill_diagonal(mat, spring_constants)
    return np.matrix(mat)


def solve_system(
    num_springs: int,
    num_masses: int,
    spring_constants: List[float],
    masses: List[float],
    fix_top: bool,
    fix_bottom: bool,
) -> None:

    print_system(num_springs, num_masses, fix_top, fix_bottom)

    A = return_difference_matrix(num_springs, num_masses, -(num_springs >= num_masses))
    _, s, _ = np.linalg.svd(A)
    print(f"l2-condition of A: {max(s) / min(s):.4f}.")

    C = return_spring_constant_matrix(spring_constants)
    _, s, _ = np.linalg.svd(C)
    print(f"l2-condition of C: {max(s) / min(s):.4f}.")

    _, s, _ = np.linalg.svd(A.transpose())
    print(f"l2-condition of A transpose: {max(s) / min(s):.4f}.")

    f = return_force_vector(masses)

    return np.linalg.pinv(A.transpose() * C * A) * f


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Spring mass solver.")
    parser.add_argument(
        "--num_springs",
        type=int,
        default=4,
        help="The number of springs in the system.",
    )
    parser.add_argument(
        "--num_masses", type=int, default=3, help="The number of masses in the system."
    )
    parser.add_argument(
        "--spring_constants",
        type=str,
        default="1,1,1,1",
        help="The spring constants of the springs in the system.",
    )
    parser.add_argument(
        "--masses",
        type=str,
        default="1,1,1",
        help="The actual masses of the masses in the system.",
    )
    parser.add_argument(
        "--fix_top",
        action="store_true",
        help="Whether the top spring is connected to a fixed end",
    )
    parser.add_argument(
        "--fix_bottom",
        action="store_true",
        help="Whether the bottom spring is connected to a fixed end",
    )
    args = parser.parse_args()

    # Do some general args processing to ensure a feasible system.
    spring_constants = [float(c.strip()) for c in args.spring_constants.split(",")]
    assert (
        len(spring_constants) == args.num_springs
    ), "Ensure the number of springs and number of spring constants is equal!"

    masses = [float(c.strip()) for c in args.masses.split(",")]
    assert (
        len(masses) == args.num_masses
    ), "Ensure the number of physical masses and number of supplied masses is equal!"

    displacements = solve_system(
        args.num_springs,
        args.num_masses,
        spring_constants,
        masses,
        args.fix_top,
        args.fix_bottom,
    )

    print(f"Displacements for the system:\n {displacements}")
