**This File briefly ecompares and explains the improvements along with the new additons done to this application in the Phase II Development**

|  Improvements | Phase I   | Phase II  |
| ------------ | ------------ | ------------ |
| Error Handling ( Test cases)| Multiple issues with error handling and Continous fails in running the test code in local | Fixed all the issues with test files and imlemented very detailed error handling for all existing and new features|
|Handling all use cases (Test)|Test cases did not cover many existing use cases (Eg. Profanity)| Covered all the use cases from Phase I |
|Restricting access (Feature)|Instructor channel were accessible and visible to all members | Restricted access to Instructors|
|Hosted in Heroku (Deployment)|Had to run the bot locally | Hosted in heroku for better convenience and higher consistency|
|QnA handling (Database)| Did not check for repeating questions| Storing the QnAs in DB to handle repetiton|
| Read me and feature docs (Documentation)| Had phase 1 details in Read me but no deparate file explaining functions|The new docs have updated feature descriptions and function descriptions in isolation|

|  New Commands/ Features | Details  |
| ------------ |------------ |
| Poll | Poll functionality for administrators   |
|   Ping|Shows latency for debugging  |
|Stats | Shows stats like	|
|Attendance| Finds attendees and absentees of class|
|Member Join|run when member joins a guild in which bot is alreay present|
|Member Quit or Removal|run when member leaves a guild in which bot is alreay present|
|Get Instructor|Command used to give Instructor role out by instructors|
|Remove Instructor|Command used to remove a user from Instructor role by instructors|
| custom-profanity|Define a word to be added to the profanity filter|
