from pathlib import Path

from src.TimecodeClass import Timecode
from src.timeShift import runTimeShift

# Paths and configuration
INPUT_FOLDER = Path("Input/Folder/Here")
OUTPUT_FOLDER = Path("Output/Folder/Here")

TIMESHIFTAFTER = Timecode("00:12:35,000")
DURATION = Timecode("00:00:10,000")

# Ensure the output folder exists
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# Process each .srt file in the input folder
for infile in INPUT_FOLDER.glob("*.srt"):
    # Define the output file path
    outfile = OUTPUT_FOLDER / infile.name

    # Apply the time shift
    runTimeShift(infile, outfile, TIMESHIFTAFTER, DURATION)

    print(f"Processed {infile.name}")

print("All files have been processed.")
