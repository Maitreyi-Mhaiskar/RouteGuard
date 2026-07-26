# RouteGuard

BGP Prefix Hijacking Detection and Automated Mitigation Framework


## Motivation

BGP is vulnerable to prefix hijacking attacks where malicious ASes
announce IP prefixes they do not own.


## Features

✓ BGP topology simulator

✓ Prefix hijacking attack simulation

✓ Route anomaly detection

✓ Automated mitigation rule generation

✓ Monitoring dashboard


## Architecture


AS1 ---- AS2
 |
AS3
 |
AS4(attacker)


        |
        |
 RouteGuard Detector


## Installation


git clone <repo-url>

cd RouteGuard

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt



## Running the Demo


1. Create normal BGP announcement

python simulator/topology.py


2. Launch hijacking attack

python simulator/attack.py


3. Detect attack

python detector/hijack_detector.py


4. Start dashboard

python dashboard/app.py


Open:

http://localhost:5000


## Example Output


HIJACK DETECTED

Expected AS:
1

Received AS:
4


## Technologies

Python
Flask
NetworkX
BGP Routing Concepts
