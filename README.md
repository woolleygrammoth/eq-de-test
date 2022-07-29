# EQ Data Engineering Exercise

## Usage
### Building the container: 
1. Open terminal and navigate to eq-de-test. 
    !docker build -t eq-de-test . 
    !docker run -it -d --restart unless-stopped eq-de-test 
    !docker ps 
2. Copy the container id from the output and include it below: 
    !docker exec {{container id}} python3 main.py
3. Open a shell inside the container: 
    !docker attach {{container id}}
4. View the output files as in a normal shell
   - Mac/Linux
        !cat raw.json
        !cat forecast-5d-3h.csv
    - Windows
        !type raw.json
        !type forecast-5d-3h.csv

__Optional__
5. To run the data fetching unit test from outside the container: 
    !docker exec {{container id}} python3 test-fetch.py
6. To retrieve and save fresh data from outside the container: 
    !docker exec {{container id}} python3 main.py

## Contents

#### config.py 
Stores credentials and specs for the API call

#### DETake-homeexercise.pdf
The instructions for this assessment. 

#### Dockerfile 
Docker build instructions

#### fetch.py
Defines the function used to call the API. 

#### main.py
Execution performs steps 1-7 of this exercise

#### README.md
This file

#### requirements.txt
Project requirements to be installed

#### test-fetch.py
Execution performs a unit test for the API call function. 
