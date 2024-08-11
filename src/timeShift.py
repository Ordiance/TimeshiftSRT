import re
from pathlib import Path
from typing import List

from src.SubtitleClass import Subtitle
from src.TimecodeClass import Timecode


# Function to parse the SRT file
def parseSRT(infile: Path) -> list:
    subtitles = []

    with open(infile, "r", encoding="utf-8") as file:
        content = file.read()

        # Splitting the content into blocks#
        blocks = content.strip().split("\n\n")

        for block in blocks:
            index, startTime, endTime, content = parseSubtitle(block)

            print(f"Start Time: {startTime}")
            print(f"End Time: {endTime}")
            print(f"Content: {content}'\n")

            # Adding the subtitle to the list
            subtitles.append(Subtitle(index, startTime, endTime, content))

    return subtitles


def parseSubtitle(block: List[str]):
    lines = block.split("\n")

    if len(lines) >= 3:
        index = lines[0]

        # Extracting the time information
        timeLine = lines[1]
        timeMatch = re.match(
            r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})",
            timeLine,
        )

        if timeMatch:
            startTime = Timecode(timeMatch.group(1))
            endTime = Timecode(timeMatch.group(2))

            # Extracting the content (all lines after the time info)
            contentLines = lines[2:]
            content = "\n".join(contentLines)

            return index, startTime, endTime, content

        raise ValueError(f"Could not identify timings for: {lines}")

    raise ValueError(f"Incorrect data passed for parsing. Received: {lines}")


def editSubtitles(
    subtitles: List[Subtitle], timeshiftAfter: Timecode, duration: Timecode
) -> List[Subtitle]:
    newSubtitles = []
    for subtitle in subtitles:
        edited = applyTimeShift(subtitle, timeshiftAfter, duration)
        newSubtitles.append(edited)

    return newSubtitles


def applyTimeShift(
    subtitle: Subtitle,
    timeShiftAfter: Timecode,
    duration: Timecode,
):
    startTime = subtitle.getStartTime()
    endTime = subtitle.getEndTime()
    content = subtitle.getContent()

    if startTime.getTotalTime() > timeShiftAfter.getTotalTime():
        startTimeTotal = startTime.getTotalTime()
        endTimeTotal = endTime.getTotalTime()
        durationTotal = duration.getTotalTime()

        # Saving old timings only for logging purposes
        oldStart = str(startTime)
        oldEnd = str(endTime)

        # Add together the totalTime (in ms) with the input time shift duration for both startTime & endTime
        startTime.setTotalTime(startTimeTotal + durationTotal)
        endTime.setTotalTime(endTimeTotal + durationTotal)

        subtitle.setStartTime(startTime)
        subtitle.setEndTime(endTime)

        print(f"Retimed subtile [{subtitle.getIndex()}] with content:")
        print(content)
        print(f"StartTime: {oldStart} ----> {startTime}")
        print(f"EndTime: {oldEnd} ----> {endTime}\n")

    else:
        print(f"Skipped subtile [{subtitle.getIndex()}] with content:")
        print(content)
        print(f"StartTime: {startTime}")
        print(f"EndTime: {endTime}\n")

    return subtitle


def writeSRT(subtitles: List[Subtitle], outfile: Path) -> None:
    with open(outfile, encoding="utf-8", mode="w") as file:
        for subtitle in subtitles:
            index = subtitle.getIndex()
            startTime, endTime = subtitle.getStartTime(), subtitle.getEndTime()
            content = subtitle.getContent()

            file.write(f"{index}\n")
            file.write(f"{startTime} --> {endTime}\n")
            file.write(f"{content}\n\n")


def runTimeShift(
    infile: Path, outfile: Path, timeshiftAfter: Timecode, duration: Timecode
):
    subtitles = parseSRT(infile)
    newSubtitles = editSubtitles(subtitles, timeshiftAfter, duration)
    writeSRT(newSubtitles, outfile)
