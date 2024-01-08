# World-Analysis
Giving eyes to machine
# Vision2 Project Documentation

## Project Overview

The `vision2` project is designed for [provide a brief overview of the project and its purpose].

## Getting Started

To get started with the `vision2` project, follow the steps below:

### Prerequisites

- Python 3.x installed
- Required Python packages (list them)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vision2.git
   cd vision2
### File Descriptions
## gemini.py
This file contains the integration with the Google Generative AI API (Gemini). It includes functions for generating text content, analyzing images, and engaging in chat conversations.

## speech.py
The speech.py file uses the Bard API to convert text content into speech and play the resulting audio. It includes functions for initializing the Bard API, retrieving audio data, and playing the audio using Pygame.

## listen.py
The listen.py file utilizes the SpeechRecognition library to capture audio from a microphone and convert it into text using Google's speech recognition service. It includes a function for capturing and recognizing speech.

## vision2.py
This is the main script that captures video frames, saves frames to an image file, analyzes the image using the gemini model, and converts the description to speech using the speech module. It also incorporates speech recognition for user input.
###  Running the  Script
* Run the main script vision2.py to start capturing video frames, analyzing images, and converting the results into speech.
 ```bash
  python vision2.py
  
```
## Keyboard Controls
Press esc to capture the current frame and perform image analysis.
Press q to exit the application.
