# Subtitle Retimer

Python scripts for individual or bulk processing & retiming .srt subtitle files based on time shift and duration values specified per episode.

## Background

These scripts are designed to automate the process of retiming subtitles across multiple episodes of a series. The retiming is based on custom time shifts and durations for each episode, provided in a template file. The script processes one/all .srt files within a specified input folder, applies the appropriate time shifts, and outputs the retimed subtitles to a designated folder.


## Template file
The `bulkTemplate.txt`-file is used by the `bulkProcess.py` script to edit multiple subtitle files at once, providing two individually configurable parameters:
- **Duration**: Specifies how much the subtitles should be time shifted.
- **Time-Shift after**: Defines the time after which the subtitles should be shifted.


## Usage

Make sure Python 3.11+ is installed. (Earlier versions will probably work as well, but have not been tested.)

### A: Individual processing
1. **Edit Paths**: Open `singleFile.py`; set INFILE to the appropriate path for the .srt you'd like to edit; set OUTFILE to a unique path for the output-file.
2. **Configure settings**: `TIMESHIFT_AFTER` sets the entry point after which subtitles are being shifted. `DURATION` sets the shift interval.
3. **Run the Script**: Execute the script to process the specified .srt file.

### B: Bulk processing
1. **Edit the Template File**: Customize the `bulkTemplate.txt` file with the appropriate time shifts and durations for your subtitle files.
2. **Configure Paths**: Open `bulkProcess.py`; Update the input and output folder paths.
3. **Run the Script**: Execute the script to process all .srt files in the input folder.


## License
This project is licensed under the MIT License - see the LICENSE file for details.