"""One bounded unchanged independent Hamming family; see TRACE-021 scope."""
from pathlib import Path
import runpy


if __name__ == '__main__':
    context = runpy.run_path(str(Path(__file__).with_name('fractional_hamming_replay.py')))
    context['main']('offcharge_bound')
