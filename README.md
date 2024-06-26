# meeple-matchmaker
A telegram bot for meeple market which matches 
"in-search-of" and sale posts and notifies users

## How does it work?
    
The bot uses two things from a posted message in the group
  
- a message tag, supported tags are: #lookingfor, #sale, #selling, #seekinginterest, #sell, #found, #sold
- a game name, the more accurately your name matches the BGG name, the better your chances of success
      
## Example:

Deepak posts a message
```
#lookingfor Ark Nova
```

Chaitanya posts a message
```
#lookingfor Ark Nova
```

Tanuj posts a message a few days later
```
#seekinginterest Ark Nova
```

The bot will reply to Tanuj's message and tag Deepak and Chaitanya
```
@Deepak @Chaitanya
```

### How do I stop the notifications?
You can use messages to do this for specific games

This command will remove you from the user list who are actively searching for Ark Nova
```
#found Ark Nova
``` 

This command will remove you from the user list who are actively selling Ark Nova
```
#sold Ark Nova
``` 

In addition, if you'd like to stop notifications for all posts
Go to the bot chat and type /disable
This will stop all tags for you for all games you've already posted about.
**Note:** This does not stop future notifications you might sign up for again


**Please do not post any feedback / comments / suggestions / bugs / requests on the Meeple Market Channel
Use the chit-chat channel or [Github](https://github.com/sahilthapar/meeple-matchmaker)**