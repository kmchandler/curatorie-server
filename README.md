# curatorie
## Topics
- [Primary Features](#primary-features)
- [Target Audience](#target-audience)
- [Purpose](#purpose)
- [Getting Started](#getting-started)
- [Contributions](#contributions)
- [Wireframe](#wireframe)
- [ERDs](#ERDs)
- [Video Walkthrough](#video-walkthrough)

<img src="styles/curatorie_screenshot.png" alt="curatorie" title="curatorie">

## Primary Features
The primary features of this product are:

App security:
  * The app is setup with security via Firebase SDK
  * The auth token is attached to the header of every api call within the app so no requests can be successfully processed if the token is not validated
    * Non-valid users are automatically redirected to the form for creation of new users 

Create a User:
  * Upon signin via Firebase Authentication, a new user is taken to the form for the creation of new users
  * When the form is submitted, the user is taken to the app's homepage, where boards will be shown, once created
  * Users can only view their own content and content that has been shared with them

Boards:
  * Users can add four different types of boards to their hompage, each with its own unique info and rendering:
    * Gift Boards:
      * Used to track items you wish to buy as a gift for others or ask for as a gift for yourself
      * Information gathered in this board type includes:
        * A link to the item webpage (which redirects to that page when clicked)
        * An url for the image you wish to display on the item card
        * Item name
        * Item description
        * Item price
        * Occasion
        * Whether the gift is for yourself or someone else
        * The name of the person who you plan to give the gift to (or who you plan to ask to give you the gift)
        * Whether or not it is a favorite or priority item (favorite/priority items appear at the top of the list of cards)
    * Inspo Boards:
      * Used to save images and info on things you are using for inspiration, such as personal style, home decor, tattoo ideas, makeup idea, etc.
      * Information gathered in this board type includes:
        * An url for the image you wish to display on the card
        * A description including additional information about how this relates to you or which part of the image you are drawn to
        * Whether or not it is a favorite or priority item (favorite/priority items appear at the top of the list of cards)
    * List Boards:
      * Used to keep track of anything you would put on a list, such as to-dos, invite/rsvp lists, places you want to go, etc.
      * This board type gathers and displays only individual list items and priority (priority items appear at the top of the list)
    * Purchase Boards: 
      * Used to tack items you wish to purchase in the near future
        * Information gathered in this board type includes:
          * A link to the item webpage (which redirects to that page when clicked)
          * An url for the image you wish to display on the item card
          * Item name
          * Item description
          * Item price
          * Whether or not it is a favorite or priority item (favorite/priority items appear at the top of the list of cards)
  * When the user clicks add board, they are taken to a page displaying a sample image of each board type where they select which type they would like to assign to that specific board before proceeding to the next page, where they enter the board name and select from a pre-set list of icons for the board
  * There is no limit to the number of each type of board that a user can add
  * Boards can be edited, deleted, and shared with other users by clicking on the three dots in the lower right corner of the board, which brings up a modal containing the repective buttons

Cards:
  * Users can add cards to each board type with specific data, based on the board type selected
  * Once created, cards can be edited or deleted

Sharing Boards:
  * Users can share boards with other users by other users by clicking on the three dots in the lower right corner of the board, which brings up a modal containing, among others, the share button
    * Clicking the share button takes the user to a page where they can search for users by first name, last name, username, or email address. Once they hit submit, all users matching the included criteria will appear on the page
      * After locating the desired user, the current user can send the board by clicking on the papar airplane icon in the lower right corner
        * If there is already an outstanding share request for that board, an error will pop up indicating that you cannot share the same board with a given user multiple times, otherwise a message will apear indicating the board was sent successfully upon the automatic re-routing to the homepage

Managing Share Requests:
  * When a user receives a request from another user wishing to share a board with them, a badge will appear on the share requests link in the navbar, indicating the number of outstanding share requests
    * If a user clicks on the share requests link, they will be taken to a page containing all boards that have been sent to them, with an option to accept or decline the invitation. If they accept the invitation, the board will be added to their shared boards page, and both users will be able to view, edit, and delete the board. If they reject the invitation, the request will be removed, and the user will lose access to the board


## Target Audience
This app is for anyone who finds themselves struggling to keep track of ideas and information. This might look like stacks of paper cluttering your space or finding yourself drowning in countless screenshots and opened browser tabs on your phone and computer.

## Purpose
curatorie is designed to help the user keep track of wish lists, to-dos, inspiration, etc. as they curate and manage their life.

## Try curatorie
1. Clone the project to your machine - git@github.com:kmchandler/curatorie.git and go into the project directory
2. Run `pipenv install` and `pipenv shell`
3. Run migrations and seed the database by running `./seed.sh`
4. To start the server, run `python manage.py runserver` (NOTE: In order for the application to work, you will also need to have the frontend repo cloned on your machine and the client running. The repo can be found [here](https://github.com/kmchandler/curatorie).)

## Contributions
This app was created by Kristen Chandler
https://github.com/kmchandler

## Wireframe
[Link to curatorie wireframe](https://whimsical.com/curatorie-5YYsV6WVUYTPYrDfs7u1Zu)

## ERD
<img src="styles/curatorie_ERD.png" alt="ERD" title="ERD">
        
## Video Walkthrough
https://www.loom.com/share/27704246c70141059dc7ac9458feae77
