"""Build and smoke-test ``dockerr/combined_mega/Dockerfile`` on Modal.

Uses the same Dockerfile + build context as local Docker::

    docker build -f dockerr/combined_mega/Dockerfile combined_mega

Run::

    modal run dockerr/combined_mega/run_on_modal.py

Requires Secret ``kx-license`` (``KDB_LICENSE_B64``) for the ``q`` check.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import modal

REPO = Path(__file__).resolve().parents[2]
DOCKERFILE = REPO / "dockerr" / "combined_mega" / "Dockerfile"
CONTEXT = REPO / "combined_mega"

app = modal.App("combined-mega-dockerfile")

# Exact local Dockerfile; context_dir mirrors ``docker build … combined_mega``.
image = modal.Image.from_dockerfile(
    DOCKERFILE,
    context_dir=CONTEXT,
).entrypoint(["/opt/kx/with-kx-license"])

kx_license = modal.Secret.from_name("kx-license", required_keys=["KDB_LICENSE_B64"])


@app.function(image=image, secrets=[kx_license], timeout=600)
def smoke() -> str:
    lines: list[str] = []

    py_out = subprocess.check_output(
        ["python", "-c", "import sys; print(sys.version.split()[0])"],
        text=True,
    ).strip()
    lines.append(f"python => {py_out}")

    q_out = subprocess.check_output(["q", "-q"], input=b"1+1\n").decode().strip()
    if q_out != "2":
        raise RuntimeError(f"q 1+1 expected '2', got {q_out!r}")
    lines.append(f"q 1+1 => {q_out}")

    help_out = subprocess.run(["a2q", "-h"], capture_output=True, text=True)
    combined = help_out.stdout + help_out.stderr
    if "AQuery Compiler" not in combined:
        raise RuntimeError(f"a2q -h unexpected output:\n{combined}")
    lines.append("a2q -h => AQuery Compiler (ok)")

    for cmd in (
        ["java", "-version"],
        ["uv", "--version"],
        ["ruff", "--version"],
        ["ty", "--version"],
        ["psql", "--version"],
        ["postgres", "--version"],
        ["reprozip", "--version"],
        ["duckdb", "-c", "SELECT 1;"],
    ):
        proc = subprocess.run(cmd, capture_output=True, text=True, check=True)
        out = (proc.stdout or proc.stderr).strip().splitlines()[0]
        lines.append(f"{cmd[0]} => {out}")

    duckdb_py = subprocess.check_output(
        ["python", "-c", "import duckdb; print(duckdb.__version__)"],
        text=True,
    ).strip()
    lines.append(f"duckdb (python) => {duckdb_py}")

    return "\n".join(lines)


@app.local_entrypoint()
def main() -> None:
    print(smoke.remote())
