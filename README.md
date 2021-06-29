# Spoonacular Food API

### [Purpose](#Purpose)
### [Major component](#Major_Component)
### [System Requirements](#System_Requirements)
### [Installation Guide](#Installation_Guide)
### [Features and project walkthrough](#Features_and_project_walkthrough)
### [Design Decisions](#Design_Decisions)
### [References](#References)

## Purpose:
Python application to accept ingredients from the user and fetch the appropriate recipes using spoonacular food API.

## Major_Component:
- Python Command Line Interface
- Python programming language

## System_Requirements:
1. Python 3.8 or above
2. Requests 2.25.1
3. Python-dotenv 0.18.0

## Installation_Guide:
Step-1. Clone the project Repo.

Step-2. Unzip the downloaded folder.

Step-3. Open the terminal and navigate to the project's root folder and run the following commands

pip3 install -r requirements.txt 


## Features_and_project_walkthrough:
Step-1. Run th main.py file using the following command via terminal

python3 main.py

Step-2. Users will able to provide the ingredients (comma-separated) via a command-line interface(CLI).

Step-3. The application will fetch one recipe featuring used ingredients as well as missing ingredients required for that particular dish.

Step-4. At this point, the user will receive an option to either like the displayed recipe or go for a new one, If the user doesn't like the recipe then the application will repeat step 3 and so on, and if the user likes the recipe, the missing ingredients will be added to the shopping list, providing an option for viewing more recipes. If the user want to view more then goto step 3.;

Step-5. If the user decided not to view more recipes, then the application will display the final shopping list, which aisles the user needs to visit along with the estimated cost of the shopping lits.


## Design_Decisions:
- Data stored in the memory: 
    1. As the data is limited and very small, I have stored data in memory rather than an external database.
- Python-dotenv
    1. To secure the API key used, I have added the key to the env file which won't be uploaded to version control.
    2. Provided env.example file in the git repository which explains to users how to create and use their respective API key
