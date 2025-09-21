### Subtitle Retimer Tool 

A Python command-line tool to Shift Subtitle timings in '.srt' files. 

## Features 

- shift subtitle timings forward or backbward (milliseconds). 
- Option to update the original file or create a new one. 


## Installation 
1. Clone the repository: 
'''bash 
  git clone https://github.com/TwiceHere/Subtitle-Re-timer.git

2. Navigagte to the project folder
  cd-your-repo


## Usage

'python main.py -s <milliseconds> [-i] <filepath>'

## Arguments 
1. '-s','--shift' (required): Shift time in milliseconds (can be negative). 
2. '-i','--inline'(optional): Update the original subtitle file instead of creating a new one. with Updated -prefix. 

## Examples
1. Shift subtitle forward by 500ms and create a new file prefixed "Update"
'python main.py -s 500  my_subtitles.srt'

2. Shift subtitle backward by 500ms and create a new file prefixed "Update"
'python main.py -s -500  my_subtitles.srt'

3. Shift subtitle forward by 500ms and Modify the original file 
'python main.py -s 500  -i my_subtitles.srt'

3. Shift subtitle backward by 500ms and Modify the original file
'python main.py -s -500  -i my_subtitles.srt'
