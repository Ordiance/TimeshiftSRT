import re
from pathlib import Path
from typing import Dict

from src.TimecodeClass import Timecode
from src.timeShift import runTimeShift

# Paths
INPUT_FOLDER = Path("Input/Folder/Here")
OUTPUT_FOLDER = Path("Output/Folder/Here")
TEMPLATE = Path("./bulkTemplate.txt")


# Function to parse the template file
def parseTemplate(templateFile: Path) -> Dict[str, Timecode]:
    with open(templateFile, "r", encoding="utf-8") as file:
        lines = file.readlines()

    durationMap = {}
    timeshiftMap = {}
    currentSection = None

    for line in lines:
        # Skip empty lines
        if line.strip() == "":
            continue

        # Determine the current section based on the header lines
        if "Duration" in line:
            currentSection = "duration"
            continue
        elif "Time-Shift after" in line:
            currentSection = "timeshift"
            continue

        # Extract episode number and corresponding timecode
        episodeMatch = re.match(r"(\d+)\s+(\d{2}:\d{2}:\d{2},\d{3})", line)
        if episodeMatch:
            episode = int(episodeMatch.group(1))
            timecode = Timecode(episodeMatch.group(2))

            if currentSection == "duration":
                durationMap[episode] = timecode
            elif currentSection == "timeshift":
                timeshiftMap[episode] = timecode

    if not durationMap or not timeshiftMap:
        raise ValueError("Template file is missing required data")

    return durationMap, timeshiftMap


# Main processing logic
def processSubtitles(inputFolder: Path, outputFolder: Path, templateFile: Path):
    # Parse the template file
    durationMap, timeshiftMap = parseTemplate(templateFile)

    # Process each .srt file in the input folder
    for infile in inputFolder.glob("*.srt"):
        # Extract the episode number from the filename
        episodeMatch = re.search(r"(\d+)", infile.stem)
        if episodeMatch:
            episode = int(episodeMatch.group(1))

            if episode in durationMap and episode in timeshiftMap:
                timeshiftAfter = timeshiftMap[episode]
                duration = durationMap[episode]

                # Define the output file path
                outfile = outputFolder / infile.name

                # Apply the time shift
                runTimeShift(infile, outfile, timeshiftAfter, duration, False)

                print(f'Processed "{infile.name}" for Episode {episode} with settings:')
                print(f"Time-Shift after: {timeshiftAfter}")
                print(f"Duration: {duration}\n")

    print("All files have been processed.")


# Execute the script
processSubtitles(INPUT_FOLDER, OUTPUT_FOLDER, TEMPLATE)
