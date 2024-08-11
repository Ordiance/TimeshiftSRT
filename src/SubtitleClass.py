from src.TimecodeClass import Timecode


class Subtitle:
    def __init__(
        self, index: int, startTime: Timecode, endTime: Timecode, content: str
    ):
        self.index = index
        self.startTime = startTime
        self.endTime = endTime
        self.content = content

    def getIndex(self):
        return self.index

    def setIndex(self, index):
        if not isinstance(index, int) or index < 0:
            raise ValueError("Index must be a non-negative integer.")
        self.index = index

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, startTime):
        if not isinstance(startTime, Timecode):
            raise ValueError("Start time must be a Timecode instance.")
        self.startTime = startTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, endTime):
        if not isinstance(endTime, Timecode):
            raise ValueError("End time must be a Timecode instance.")
        self.endTime = endTime

    def getContent(self):
        return self.content

    def setContent(self, content):
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        self.content = content

    def __str__(self):
        return self.content
