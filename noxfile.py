import os
from pathlib import Path

import nox

requirements_files = list(
    {path.name.replace(".in", "") for path in Path("tests").glob("*in")}
    - {"constraints", "constraints-base"}
)


@nox.session(name="pip-compile", python=["3.11"])
@nox.parametrize(["req"], requirements_files, requirements_files)
def pip_compile(session: nox.Session, req: str):
    # .pip-tools.toml was introduced in v7
    session.install("pip-tools >= 7")

    # Use --upgrade by default unless a user passes -P.
    args = list(session.posargs)
    if not any(
        arg.startswith("-P") or arg.startswith("--upgrade-package") for arg in args
    ):
        args.append("--upgrade")

    session.run(
        "pip-compile",
        "--output-file",
        f"tests/{req}.txt",
        *args,
        f"tests/{req}.in",
    )
