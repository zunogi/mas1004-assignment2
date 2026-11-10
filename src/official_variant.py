"""Run official.py with an isolated recipe directory."""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recipe-dir", required=True)
    parser.add_argument("--selection")
    args, official_args = parser.parse_known_args()
    recipe_dir = (ROOT / args.recipe_dir).resolve()
    if ROOT not in recipe_dir.parents or not (recipe_dir / "recipe.py").is_file():
        raise SystemExit(f"invalid recipe directory: {args.recipe_dir}")
    if not args.selection:
        env = {**os.environ, "MAS1004_RECIPE_DIR": str(recipe_dir)}
        result = subprocess.run(
            [sys.executable, "-u", str(ROOT / "src" / "official.py"), *official_args],
            cwd=ROOT,
            env=env,
            check=False,
        )
        raise SystemExit(result.returncode)

    selection = (ROOT / args.selection).resolve()
    if ROOT not in selection.parents or not selection.is_file():
        raise SystemExit(f"invalid selection file: {args.selection}")
    with tempfile.TemporaryDirectory(prefix="track_a_recipe_", dir=ROOT / "results") as temporary:
        run_recipe_dir = Path(temporary)
        shutil.copy2(recipe_dir / "recipe.py", run_recipe_dir / "recipe.py")
        shutil.copy2(selection, run_recipe_dir / "selection.csv")
        env = {**os.environ, "MAS1004_RECIPE_DIR": str(run_recipe_dir)}
        result = subprocess.run(
            [sys.executable, "-u", str(ROOT / "src" / "official.py"), *official_args],
            cwd=ROOT,
            env=env,
            check=False,
        )
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
