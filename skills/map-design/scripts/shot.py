"""Render a map HTML file to PNG with headless Chrome, Edge or Chromium.

python shot.py map.html [out.png] [--height 760] [--dark]
"""
import os, shutil, subprocess, sys, tempfile
from pathlib import Path

CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome", "chromium", "chromium-browser", "microsoft-edge",
]


def browser():
    for c in CANDIDATES:
        p = c if os.path.isfile(c) else shutil.which(c)
        if p:
            return p
    sys.exit("no Chrome, Edge or Chromium found; set CHROME=/path/to/browser")


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    height = int(argv[argv.index("--height") + 1]) if "--height" in argv else 760
    if "--height" in argv:
        args.remove(str(height))
    src = Path(args[0]).resolve()
    out = Path(args[1] if len(args) > 1 else src.with_suffix(".png")).resolve()
    url = src.as_uri() + ("#dark" if "--dark" in argv else "")
    with tempfile.TemporaryDirectory() as prof:
        subprocess.run([os.environ.get("CHROME") or browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        f"--window-size=1150,{height}", "--virtual-time-budget=15000", f"--user-data-dir={prof}",
                        f"--screenshot={out}", url], check=True, capture_output=True)
    print(out)


if __name__ == "__main__":
    main(sys.argv[1:])
