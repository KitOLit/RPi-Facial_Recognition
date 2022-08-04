# Facial Recognition with Raspberry Pi

To build a Facial Recognition System using a Raspberry Pi and a Pi Camera. 

## Tasks

| Task | Milestone     | Date              |
| :-------- | :------- | :------------------------- |
| `ML Algorithm` | `Milestone 1` | **04/08/2022** |
| `Prototype test` | `Milestone 1` | **06/08/2022** |
| `Design and Print Model` | `Milestone 2` | **08/08/2022** |
| `Full Working Prototype` | `Milestone 3` | **08/08/2022** |

## Installation

Install all the requirements for the project by running

``` bash Install/install.bash ```
## Appendix

The system uses a Raspberry Pi connected to the internet and a Pi Camera. 

To run the model 
``` python3 main.py ```: This runs the model with accordance to the encodings saved in a pickle file.

To train the model
``` python3 trainModel.py``` : This trains the model with available faces in the dataset folder.

To capture new face shots
``` python3 facePhotoDatasetCreator.py```: This captures 10-15 photos of the face to be recognized and stores it under the dataset folder with the name given in the file.

## DEMO

TO BE ADDED SOON