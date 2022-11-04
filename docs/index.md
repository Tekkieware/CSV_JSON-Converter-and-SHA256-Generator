<h2> About Script </h2>
This script accepts a CSV(Comma seperated value) file as input, 
generates a JSON(javascript object notation) file for each row in the CSV file, generates a sha256 hash for each file, 
appends the hash to each JSON and creates a new copy of the CSV file with a new column included for the hash of the JSON generated for each row.

<b>Language:</b> Python.
<b>Python Version:</b> 3.10
<b>Dependencies:</b> No external library needed.

<h2>How To Use</h2>
<b>Not Before</b>: Please clear all empty columns in the spreadsheet before generating the CSV file to avoid trailing commas 
which will add empty keys to the JSON generated with this script.

<h2>Follow These Steps To Use Script:</h2>
<ul>
  <li>Copy your CSV file into the Input CSV file folder.</li>
  <li>Run the logic.py python file.</li>
  <li>You will be prompted to enter the name of your CSV file in the terminal, please enter it correctly e.g NFT Naming csv - All Teams.csv.</li>
  <li>Wait for the process to complete and you will find the output files in the Ouput CSV File and Output JSON Files folders.</li>
 </ul>
