"""Regenerate and execute max_loss.generated.q on Modal.

Run from the repository root:
    modal run example/hw1_11/run_on_modal.py
"""

from pathlib import Path
import subprocess

import modal

ROOT = (
    Path(__file__).resolve().parents[2] if modal.is_local() else Path("/")
)
AQUERY = ROOT / "aquery"
EXAMPLE = ROOT / "example" / "hw1_11"

app = modal.App("aquery-hw1-11")
image = modal.Image.from_dockerfile(
    AQUERY / "docker-x86-linux" / "Dockerfile",
    context_dir=AQUERY,
)
if modal.is_local():
    image = image.add_local_dir(EXAMPLE, remote_path="/work")

kx_license = modal.Secret.from_name(
    "kx-license", required_keys=["KDB_LICENSE_B64"]
)


@app.function(image=image, secrets=[kx_license], timeout=10 * 60)
def verify() -> str:
    generated = Path("/work/max_loss.generated.q")
    generated.unlink(missing_ok=True)

    subprocess.run(
        ["a2q", "-c", "-a", "1", "-o", generated.name, "max_loss.a"],
        cwd="/work",
        check=True,
    )
    q_result = subprocess.run(
        ["/opt/kx/with-kx-license", "q", generated.name],
        cwd="/work",
        text=True,
        capture_output=True,
        check=True,
    )
    return (
        f"compile: ok\ngenerated: {generated.stat().st_size} bytes\n"
        f"q output:\n{q_result.stdout}{q_result.stderr}"
    )


@app.local_entrypoint()
def main() -> None:
    print(verify.remote())
