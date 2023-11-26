**This File briefly ecompares and explains the improvements along with the new additons done to this application in the Phase II Development**

|  Improvements | Phase I   | Phase II  |
| ------------ | ------------ | ------------ |
| Test case error handling | Test cases had many local hard coded variables and was falining when running in a local windows system. Also some existing test cases were failing. | Fixed all the issues with test files and added support for running in windows. Made sure the hard coded values are made as variables in the .env file to be uploaded as input. |
| Handling all use cases (Test) | Test cases did not cover many existing use cases (Eg. Profanity) | Covered all the use cases from Phase I and wrote cases to handle newly added features. |
| Restricting access (Feature) | Instructor channel visible and accesible to all members. | Restricted instructor channel access to only instructors and when a instructor is remove and re-added made sure the chats inthe period he wans't available is not accessible to him. |
| Hosted in Heroku (Deployment) | Had to run the bot locally | Hosted in heroku for better convenience and higher consistency. |
| QnA handling (Database) | Did not store questions and answers in a database | created database to store QnAs. |
| Read me and feature docs (Documentation) | Had phase 1 details in Read me but no separate file explaining functions | The new docs have updated feature descriptions and function descriptions in isolation |
| Office Hour run | Office hour run in the very first time after BOT is added/re-added to the server raises a Key error even if database has values. | Fixed the same, by making sure the check is run only after the database populates the BOT's local variables |
| Create events and office hours | The bot always threw an error when trying to create a new event/ office hour as the BOT waiting time for a response was very less. | Modified the code to wait for longer duration to recieve user input before throwing error. |
| Instructor check before adding | Previous blindly tried to add instructor. Shows a success message even if the member already had a instructor role. | Modified code to check if the person was already an instructor and outputs information accordingly. |
| Text channels recreating | If the bot is added to a server it recreated some default channels each time again and again. | Code changes to check for the existence of the channel before adding it. |
| Help | Used inbuild discord help | Added custom help command to better suite the usage. |

# Phase V  
|  New Commands/ Features | Details |
| ------------ |------------ |
| Custom profanity settings | Whenever a user enters an nsfw message, the user can be warned, timed-out and even blocked from the server as per the settings of the instructor or the default settings which is warning, followed by timeout followed by ban from server.|
| Persistent Block from server |  If a user is banned and kicked out from the server they remain blocked, if they try to join the server when the bot is not running, it will kick them out when the bot starts up. If they try to join again when the bot is running, it will not let them join the server.|
| !unblock_user | A new command which allows instructors to have the power to unblock users just by using their usernames to allow banned people to join back in.|
| DB initialization | The bot was integrated properly with the DBs in use, as any new user joins when the bot is not running or so, it makes no entry of the user and struggles with error. In the initialization phase, we have even set up to detect all the users in the server and make database entries for each user whose entry does not exist |
| Spam Violation penalty | Each user gets some points for sending a message which increases the xp and at each 100 xp it goes up a rank. However, they were never penalized for improper behavior. Now if the user spams, they get a penalty of 10xp. Along with getting timeouts.|
| NSFW violation penalty | Each user is given a custom penalty to their XP set by the instructor when they post a NSFW message on the chat channel.|
| !Award XP | Instructors can use this in the instructor channel to award XP to users for encouraging some behaviors.|
| !Penalize XP | Instructor can use this new command to reduce XP for any reason they seem fit such as invalid input or irrelevant discussion.|
| !Leaderboard | There is a new command that any user can run to see the leaderboard of top 10 rankers based on their ranks and XP in the group.|
| QNA Channel |  If any user tags any instructor or refer instructors, the Question will pop up in the instructor QNA channel and once they reply to the message in that channel it will be posted back to the main channel. It will help ensure that no question goes unnoticed as all the questions are available to see at one glance with no clutter in a separate channel.|

