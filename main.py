"""Write one printer apology to the configured output directory.
Staples give the jam a real cause and 'delicious' supplies the final twist.
Reject lines longer than 120 characters before writing the entry.
Write the UTF-8 bytes directly so no trailing newline is added.
"""

import os
from pathlib import Path


LINE = "Sorry for the jam — your staples were delicious"

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 120:
    raise ValueError("The entry line must be at most 120 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
