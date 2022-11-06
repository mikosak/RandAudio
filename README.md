# RandAudio
Python script that plays audio at random intervals.

## Requirements

Requires python as well as the external playsound module.

Install python by visiting the [official site](https://www.python.org/downloads/).

Install playsound with the command prompt using:
```
 pip install playsound
```

The program will attempt to install playsound if it is not installed.

## How to use

Place .mp3 files in the same folder as main script. Run the main script, enter minimum and maximum intervals and then press the play button. 
A random .mp3 is chosen and played in a seperate thread and is stopped using the stop button.
