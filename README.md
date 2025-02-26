## Exercise Tracker (Day 38)
### About
This project uses Nutritionix Natural Language API to get information about calories burned and duration of exercise from user's input. 

### How to run the project
1. Create a nutritionix account here https://developer.nutritionix.com/
2. Signup for your api key and view api key from the link above. Update APP_ID and API_KEY under Edit Configurations -> Environment Variables with the values. 
3. Create a Sheety account and link it to your email account. Create a new spreadsheet and link it to a Sheety project. 
4. Go to Edit Configurations -> Environment Variables and update SHEET_ENDPOINT and TOKEN 
5. Run `main.py` which will ask for user input about the type of exercise. The program will take the user input and update the google spreadsheet with date, time, exercise, duration and calories burned from the exercise. 
