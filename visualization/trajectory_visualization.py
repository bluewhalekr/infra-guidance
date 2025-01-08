# <Copyright 2022, Argo AI, LLC. Released under the MIT license.>
"""Script to generate dynamic visualizations from a directory of Argoverse scenarios."""
import os
from enum import Enum, unique
from pathlib import Path
from random import choices
from typing import Final

import click
from joblib import Parallel, delayed
from rich.progress import track

from av2.datasets.motion_forecasting import scenario_serialization
from av2.datasets.motion_forecasting.viz.scenario_visualization import (
    visualize_scenario,
)
from av2.map.map_api import ArgoverseStaticMap
import argparse

_DEFAULT_N_JOBS: Final[int] = -2  # Use all but one CPUs


@unique
class SelectionCriteria(str, Enum):
    """Valid criteria used to select Argoverse scenarios for visualization."""

    FIRST: str = "first"
    RANDOM: str = "random"


def generate_scenario_visualizations(
    argoverse_scenario_dir: Path,
    viz_output_dir: Path,
    num_scenarios: int,
    selection_criteria: SelectionCriteria,
    *,
    debug: bool = False,
) -> None:
    """Generate and save dynamic visualizations for selected scenarios within `argoverse_scenario_dir`.

    Args:
        argoverse_scenario_dir: Path to local directory where Argoverse scenarios are stored.
        viz_output_dir: Path to local directory where generated visualizations should be saved.
        num_scenarios: Maximum number of scenarios for which to generate visualizations.
        selection_criteria: Controls how scenarios are selected for visualization.
        debug: Runs preprocessing in single-threaded mode when enabled.
    """
    Path(viz_output_dir).mkdir(parents=True, exist_ok=True)
    all_scenario_files = sorted(argoverse_scenario_dir.rglob("*.parquet"))
    scenario_file_list = (
        all_scenario_files[:num_scenarios]
        if selection_criteria == SelectionCriteria.FIRST
        else choices(all_scenario_files, k=num_scenarios)
    )  # Ignoring type here because type of "choice" is partially unknown.

    # Build inner function to generate visualization for a single scenario.
    def generate_scenario_visualization(scenario_path: Path) -> None:
        """Generate and save dynamic visualization for a single Argoverse scenario.

        NOTE: This function assumes that the static map is stored in the same directory as the scenario file.

        Args:
            scenario_path: Path to the parquet file corresponding to the Argoverse scenario to visualize.
        """
        scenario_id = scenario_path.stem.split("scenario_")[-1]
        static_map_path = (
            scenario_path.parents[0] / f"log_map_archive_{scenario_id}.json"
        )
        viz_save_path = viz_output_dir / f"{scenario_id}.mp4"

        scenario = scenario_serialization.load_argoverse_scenario_parquet(scenario_path)
        static_map = ArgoverseStaticMap.from_json(static_map_path)
        visualize_scenario(scenario, static_map, viz_save_path)

    # Generate visualization for each selected scenario in parallel (except if running in debug mode)
    if debug:
        for scenario_path in track(scenario_file_list):
            generate_scenario_visualization(scenario_path)
    else:
        Parallel(n_jobs=_DEFAULT_N_JOBS)(
            delayed(generate_scenario_visualization)(scenario_path)
            for scenario_path in track(scenario_file_list)
        )

def parse_args():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--src_dir",
        type=str,
        default=None,
        required=True,
        help="Path to source directory.",
    )
    parser.add_argument(
        "--dst_dir",
        type=str,
        default=None,
        required=True,
        help="Path to destination directory.",
    )
    parser.add_argument(
        "--num-scenarios",
        type=int,
        default=5,
        required=False,
        help="number of scenario",
    )
    parser.add_argument(
        "--selection-criteria",
        type=str,
        default='random',
        required=False,
        help="Controls how scenarios are selected for visualization - either the first available or at random",
    )    
    args = parser.parse_args()
    return args

def run_generate_scenario_visualizations(
    argoverse_scenario_dir: str,
    viz_output_dir: str,
    num_scenarios: int,
    selection_criteria: str,
    debug: bool,
) -> None:
    """Click entry point for generation of Argoverse scenario visualizations."""
    generate_scenario_visualizations(
        Path(argoverse_scenario_dir),
        Path(viz_output_dir),
        num_scenarios,
        SelectionCriteria(selection_criteria.lower()),
        debug=debug,
    )


if __name__ == "__main__":
    args = parse_args()
    os.makedirs(args.dst_dir, exist_ok=True)
    run_generate_scenario_visualizations(args.src_dir, args.dst_dir, args.num_scenarios, args.selection_criteria, False)
