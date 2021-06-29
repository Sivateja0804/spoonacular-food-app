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
*Prerequisite: Needs Python 3.8 to be installed.* 
1. Requests 2.25.1
2. Python-dotenv 0.18.0
3. Spoonacular API Key

To install python 3.8 on Windows/Mac/Linux, go to Python official download page [here](https://www.python.org/downloads/release/python-380/). Download the executable and run the executable on the machine.

To run the project on your machine, you need to follow the steps mentioned below in the installation guide. 

## Installation_Guide:
Step-1. Clone the project Repo.

Step-2. Unzip the downloaded folder.

Step-3. Open the terminal and navigate to the project's root folder and run the following command

```pip3 install -r requirements.txt```

Step-4. Create an account on https://spoonacular.com/food-api

Step-5. After you login to the account click on My Console->Profile->Show/Hide API Key and store the API Key safely

Step-6. Create .env file(It should be in the root folder: spoonacular-food-app/) similar to env.example file that I created in this root folder and replace the dummy API Key value with your API Key Value.

```API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxx"```

*Note: Never push the .env file to your github repository. So make sure you mention the filename(*.env) in .gitignore file.



## Features_and_project_walkthrough:
Step-1. Run the main.py file using the following command via terminal

```python3 main.py```

Step-2. Users will able to provide the ingredients (comma-separated) via a command-line interface(CLI).

<img src="/screenshots/Step2.png" width="300">

Step-3. The application will fetch one recipe featuring used ingredients as well as missing ingredients required for that particular dish. At this point, the user will receive an option to either like the displayed recipe or go for a new one.

<img src="/screenshots/Step3.png" width="500">

Step-4. If the user doesn't like the recipe then the application will repeat step 3 and so on.

<img src="/screenshots/Step4.png" width="500">

Step-5. If the user likes the recipe, the missing ingredients will be added to the shopping list, providing an option for viewing more recipes. If the user want to view more then goto step 3.

<img src="/screenshots/Step5.png" width="500">

Step-6. If the user decided not to view more recipes, then the application will display the final shopping list, which aisles the user needs to visit along with the estimated cost of the shopping lits.

<img src="/screenshots/Step6.png" width="500">


## Design_Decisions:
- Data stored in the memory: 
    1. As the data is limited and very small, I have stored data in memory rather than an external database.
- Python-dotenv
    1. To secure the API key used, I have added the key to the env file which won't be uploaded to version control.
    2. Provided env.example file in the git repository which explains to users how to create and use their respective API key
