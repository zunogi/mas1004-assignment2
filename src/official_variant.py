"""Run official.py with an isolated recipe directory."""

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recipe-dir", required=True)
    args, official_args = parser.parse_known_args()
    recipe_dir = (ROOT / args.recipe_dir).resolve()
    if ROOT not in recipe_dir.parents or not (recipe_dir / "recipe.py").is_file():
        raise SystemExit(f"invalid recipe directory: {args.recipe_dir}")
    env = {**os.environ, "MAS1004_RECIPE_DIR": str(recipe_dir)}
    result = subprocess.run(
        [sys.executable, "-u", str(ROOT / "src" / "official.py"), *official_args],
        cwd=ROOT,
        env=env,
        check=False,
    )
    raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
