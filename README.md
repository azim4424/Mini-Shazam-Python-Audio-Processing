# Mini-Shazam-Python-Audio-Processing

A Python-based audio matching system inspired by music recognition applications.
The project analyzes audio signals in the frequecy domain and identifies similarities between recordings using the sliding window algorithm which compares a small clip from the original audio with the full audio. A similarity score was computed to find exactly where the best match is between the clip and the original audio. 

## Features
- Audio preprocessing
- Frequency domain analysis
- Feature extraction
- Signal comparison and matching

## Technologies
- Python
- NumPy
- SciPy
- Matplotlib
- Jupyter Notebook

## Methodology
1. Load audio signal
2. Apply preprocessing
3. Extract signal features
4. Compare extracted features
5. Determine best match

## Results
You can find the exact results in the plots inside the images folder. The last plot shows that the highest similarty score was shown at time 5 seconds which was the start of the clip. 

## How to Run
1. Install requirements
2. Open the notebook or main.py
3. Run the cells or the python file

N.B: You can either run the .py file or the .ipynb (jupyter notebook) file depending on what you have installed. Please create a folder locally in your machine for the whole project with the exact same folders inside (code, images and Audio) for the .py file or the notebook to compile correctly. The images of the plots will be saved inside the images folder after running. 
