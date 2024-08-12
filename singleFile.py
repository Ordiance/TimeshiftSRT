from pathlib import Path

from src.TimecodeClass import Timecode
from src.timeShift import runTimeShift

INFILE = Path("C:/Input/File/Here.srt")
OUTFILE = Path("C:/Output/File/Here.srt")

TIMESHIFT_AFTER = Timecode("00:12:35,000")
DURATION = Timecode("00:00:10,000")

runTimeShift(INFILE, OUTFILE, TIMESHIFT_AFTER, DURATION)
