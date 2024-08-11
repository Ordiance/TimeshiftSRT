from pathlib import Path

from src.TimecodeClass import Timecode
from src.timeShift import runTimeShift

INFILE = Path("Input/File/Here")
OUTFILE = Path("Output/File/Here")

TIMESHIFT_AFTER = Timecode("00:12:35,000")
DURATION = Timecode("00:00:10,000")

runTimeShift(INFILE, OUTFILE, TIMESHIFT_AFTER, DURATION)
