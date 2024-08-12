import re


class Timecode:
    timecodePattern = r"^(\d{2}):(\d{2}):(\d{2}),(\d{3})$"

    def __init__(self, timecodeStr):
        if not re.match(self.timecodePattern, timecodeStr):
            raise ValueError(f"Invalid timecode format: {timecodeStr}")

        self.hours, self.minutes, self.seconds, self.milliseconds = (
            self._parseTimecodeStr(timecodeStr)
        )

    def _parseTimecodeStr(self, timecodeStr):
        match = re.match(self.timecodePattern, timecodeStr)
        if not match:
            raise ValueError("Invalid timecode format")

        hours = int(match.group(1))
        minutes = int(match.group(2))
        seconds = int(match.group(3))
        milliseconds = int(match.group(4))

        return hours, minutes, seconds, milliseconds

    def _constructTimecodeStr(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d},{self.milliseconds:03d}"

    def __str__(self):
        return self._constructTimecodeStr()

    def getHours(self):
        return self.hours

    def getMinutes(self):
        return self.minutes

    def getSeconds(self):
        return self.seconds

    def getMilliseconds(self):
        return self.milliseconds

    def getTimeData(self):
        return {
            "h": self.hours,
            "m": self.minutes,
            "s": self.seconds,
            "ms": self.milliseconds,
        }

    def getTotalTime(self):
        # Convert hours, minutes, seconds to milliseconds and add milliseconds
        totalMilliseconds = (
            (self.hours * 3600 * 1000)  # Hours in milliseconds
            + (self.minutes * 60 * 1000)  # Minutes in milliseconds
            + (self.seconds * 1000)  # Seconds in milliseconds
            + self.milliseconds
        )
        return totalMilliseconds

    def setHours(self, hours):
        if not 0 <= hours < 24:
            raise ValueError("Hours must be between 0 and 23.")
        self.hours = hours

    def setMinutes(self, minutes):
        if not 0 <= minutes < 60:
            raise ValueError("Minutes must be between 0 and 59.")
        self.minutes = minutes

    def setSeconds(self, seconds):
        if not 0 <= seconds < 60:
            raise ValueError("Seconds must be between 0 and 59.")
        self.seconds = seconds

    def setMilliseconds(self, milliseconds):
        if not 0 <= milliseconds < 1000:
            raise ValueError("Milliseconds must be between 0 and 999.")
        self.milliseconds = milliseconds

    def setTimeData(self, hours, minutes, seconds, milliseconds):
        self.setHours(hours)
        self.setMinutes(minutes)
        self.setSeconds(seconds)
        self.setMilliseconds(milliseconds)

    def setTotalTime(self, totalTime: int):
        if not isinstance(totalTime, int) or totalTime < 0:
            raise ValueError("Totaltime needs to be an int and larger than 0.")
        # Constants for conversion
        MS_PER_SECOND = 1000
        SECONDS_PER_MINUTE = 60
        MINUTES_PER_HOUR = 60
        SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR

        # Calculate hours, minutes, seconds, and milliseconds
        hours = totalTime // (MS_PER_SECOND * SECONDS_PER_HOUR)
        remainder = totalTime % (MS_PER_SECOND * SECONDS_PER_HOUR)

        minutes = remainder // (MS_PER_SECOND * SECONDS_PER_MINUTE)
        remainder %= MS_PER_SECOND * SECONDS_PER_MINUTE

        seconds = remainder // MS_PER_SECOND
        milliseconds = remainder % MS_PER_SECOND

        self.setTimeData(hours, minutes, seconds, milliseconds)
