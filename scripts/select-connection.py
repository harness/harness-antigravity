#!/usr/bin/env python3
"""Select a bundled, credential-free connection profile before installation."""
import argparse
from pathlib import Path
import shutil
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("profile", choices=["hosted-oauth", "local-pat"])
a = p.parse_args()
root = Path(__file__).resolve().parent.parent
shutil.copyfile(root / "config" / (a.profile + ".json"), root / "mcp_config.json")
print("Selected", a.profile, "— validate and install this source directory.")
