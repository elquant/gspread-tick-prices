# GSpread Tick Prices

This simple Python script fetches a list of ticker symbols from a Google Spreadsheet, 
retrieves their basic information (like closing price, volume, etc), 
and writes the result back to the spreadsheet. 

## Installation

`pip install -r requirements.txt`

## Authentication with Google Sheets API

You will need a `credentials.json` file whose content is required to authenticate the application with the API.
This file should be placed at the root level of this repository. If you want to place it somewhere else, please update
the `settings.py` file accordingly editing the `GOOGLE_API_CREDENTIALS_PATH` constant.

For more information on how to get the credentials file please click 
[here](https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account "GSpread Python Library").