import sys

PROTOCOL_VERSION = 2

# Protocol v2 evaluations are produced on the Linux GPU server only (CUDA,
# full test sets, pinned environment). The guard sits at import time so that
# no entry point -- CLI, pytest, ad-hoc script -- can evaluate on a Mac and
# quietly write numbers that do not belong to the protocol.
if sys.platform != "linux":
    raise SystemExit(
        f"mini-eval runs on the Linux GPU server only (this host is {sys.platform}): "
        "protocol v2 numbers are produced on the pod, with CUDA and full test sets."
    )

from mini_eval.cli import main  # noqa: F401
