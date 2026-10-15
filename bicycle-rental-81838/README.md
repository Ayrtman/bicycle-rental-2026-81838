CA1 – Bicycle Rental System
Full Name: Ayrton Manoel Melo
Student Number: 81838
Python Version: Python 3.11

Instructions for Running the Application
To run the interactive console application:
python3 main.py

Instructions for Running the Automated Tests
To run the automated unit test suite:
python3 -m unittest test_bicycle.py -v

Assumptions Made During Development
Electric Bike Surcharge: Electric bicycles include an automatic 15% surcharge over their base rental rate to account for maintenance and battery usage.
Accepted Bike Types: Bicycles are categorized into four valid types: Road, Mountain, Hybrid, and Electric.
Gear Counts: All bicycles must have at least 1 gear (positive integer).
Rental Duration: Rental hours must be a positive number greater than zero.

Foundation and AI Assistance Acknowledgment
The core structure and logic of this project were built directly upon the class activity from Week 4 (such as class initialization, alternative constructors via @classmethod, file line parsing, and the interactive console loop).
Additional concepts and techniques introduced in Week 5 (such as abstract base classes using abc.ABC, inheritance, and automated unit testing with unittest) were incorporated to complete all assignment components.
Generative AI was used as an assistive tool to help adapt the Week 4 foundation to the bicycle rental domain, structure missing edge cases for the unit tests, and verify documentation requirements in accordance with the CA1 assignment brief.