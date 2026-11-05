Ieshan Praveen

2025-2026

[Introduction [4](#introduction)](#introduction)

[Analysis [4](#analysis)](#analysis)

[Description [4](#description)](#description)

[Key Terminology [4](#key-terminology)](#key-terminology)

[Background and Problem Identification
[6](#background-and-problem-identification)](#background-and-problem-identification)

[Current System [9](#current-system)](#current-system)

[Current Solutions [10](#current-solutions)](#current-solutions)

[Requirements [13](#requirements)](#requirements)

[Design [15](#design)](#design)

[External resources [15](#external-resources)](#external-resources)

[User Interface [16](#user-interface)](#user-interface)

[Process [20](#process)](#process)

[Mathematical Formula
[20](#mathematical-formula)](#mathematical-formula)

[Optimiser [21](#optimiser)](#optimiser)

[API [24](#api)](#api)

[Object Oriented Programming
[25](#object-oriented-programming)](#object-oriented-programming)

[Database [26](#database)](#database)

[File Storage [27](#file-storage)](#file-storage)

[Player Table/Filter Table/Optimised Table
[27](#player-tablefilter-tableoptimised-table)](#player-tablefilter-tableoptimised-table)

[Technical Solution [29](#technical-solution)](#technical-solution)

[Login [30](#login)](#login)

[Register [31](#register)](#register)

[Optimised Table [32](#optimised-table)](#optimised-table)

[Loading Data [32](#loading-data)](#loading-data)

[Search Table [33](#search-table)](#search-table)

[CSV/JSON Saving [34](#_Toc221568563)](#_Toc221568563)

[Update Player List [36](#update-player-list)](#update-player-list)

[Optimiser [40](#optimiser-1)](#optimiser-1)

[Testing [44](#testing)](#testing)

[Evaluation [46](#evaluation)](#evaluation)

[Beta testing [46](#beta-testing)](#beta-testing)

[Evaluation of requirements
[49](#evaluation-of-requirements)](#evaluation-of-requirements)

[Conclusion [51](#conclusion)](#conclusion)

[Appendix [52](#appendix)](#appendix)

[Source code [52](#source-code)](#source-code)

[Login [52](#login-1)](#login-1)

[Register [54](#register-1)](#register-1)

[Main window [57](#main-window)](#main-window)

[Player Table [58](#player-table)](#player-table)

[Optimiser [61](#optimiser-2)](#optimiser-2)

[Optimised Table [73](#optimised-table-1)](#optimised-table-1)

[Filter Table [77](#filter-table)](#filter-table)

[Code Screenshots [81](#code-screenshots)](#code-screenshots)

[Login [81](#login-2)](#login-2)

[Register [82](#register-2)](#register-2)

[Main Window [83](#main-window-1)](#main-window-1)

[Player Table [84](#player-table-1)](#player-table-1)

[Optimiser [85](#optimiser-3)](#optimiser-3)

[Filter Table [86](#filter-table-1)](#filter-table-1)

[Optimised Table [87](#optimised-table-2)](#optimised-table-2)

[Bibliography [88](#bibliography)](#bibliography)

# 

# 

# Introduction

The aim of my project is to create a fantasy basketball lineup optimiser
for a colleague who is a casual fantasy basketball manager and is
looking to find an optimiser to improve his weekly performance in his
respective leagues. It would also be useful to any other basketball
managers who may want to improve their lineups in order to achieve more
points in their respective leagues.

# Analysis

## Description

Fantasy basketball is a game that is connected to real life leagues
(Most commonly the NBA but is sometimes also done with NCAA teams). The
objective is to earn the most points in a 'league' containing other
managers including the player. The player earns points by drafting (aka
selecting) real players into a fictional lineup. Players would have to
consider player positions, salary and the teams that the selected player
plays for. The players on the fantasy team would achieve points based on
their stat lines for the week which would include their points, assists,
turnovers etc.

### Key Terminology 

- Positions and Abbreviations:

  - PG (Point Guard) -- Generates offense within the team, usually has
    more assists than any other position.

  - SG (Shooting Guard) -- Usually the best shooter on the team. Would
    attempt more 3-point shots however it is different from each player

  - SF (Small forward) -- All round player expected to be able to score
    and guard any player within the court. Good small forwards usually
    have good defensive stats (blocks and steals)

  - PF (Power Forward) -- Taller player who assists in rebounding and
    guarding inside the post, however unlike centers they are also
    capable of taking shots from further away from the basket. Expect
    decent rebounding numbers and good defensive stats

  - C (Center) -- Tallest/Largest player on the team in charge of
    rebounding and scoring close shots on offense, on defence they block
    shots taken near the basket and fight for rebounds. Expect highest
    rebound and block numbers from them

  - UTIL (Utility) -- Any player from any position can be considered as
    a utility player in order to fill up space on the bench

- Stat Descriptions and Abbreviations:

  - PTS (Points) -- Points scored by a player, combines two pointers,
    three pointers and free throws

  - REB (Rebounds) -- When a player catches a missed shot off the rim or
    backboard or if the shot was blocked

  - AST (Assists) -- Any pass that directly leads to points scored

  - STL/ST (Steals) -- When the ball is taken from the opposing team
    without a shot being attempted

  - BLK (Blocked Shots) -- When the ball is deflected during a shot
    attempt

  - TO (Turnover) -- When a player loses possession of the ball without
    a shot being attempted

  - PF (Personal Fouls) -- When a player commits an action that is
    against the rules

  - FGA/FG% (Field Goals Made/Field Goal Percentage) -- The total number
    of shots taken (FGA) compared to the shots made (FG%)

  - 3PA/3P% (3 Pointers Attempted/3 Point Percentage) -- The total
    number of three-point shots taken (3PA) compared to the three-point
    shots made (3P%)

  - FTA/FT% (Free Throws Attempted/Free Throw%) -- The total number of
    free throws taken (FTA) compared to all free throws made (FT%)

## Background and Problem Identification

My end user is a college student named Aaron Sutcliffe who is a casual
fantasy sport manager. He participates in online NBA fantasy leagues as
well as in personal NBA fantasy leagues with friends.

In his respective leagues he is usually only assigned to create and
manage his own lineups as there would be commissioners who would be in
charge of league rules. He would also have to follow a different set of
rules for each respective league as each one would operate differently
with a different set of limitations.

Once he joins a league he would be asked to create his lineup of 12 NBA
players either with full control to add any player to his lineup or with
positional limitations that only allow him to have a certain number of
players from each position, usually 4 Guards, 4 Forwards and 2 Centers
and 2 Utility players

He may also have to follow a salary cap which prevents him from picking
all the best performing players as star players who gain a lot of
fantasy points will have a higher salary than role players in a team.
This would make him have to analyse what set of players would give him
the best results.

There may also be a draft system where each manager would select one
player at a time from a large draft of all NBA players so he would have
to adjust his lineup in real time in order to select the right set of
players that still remain in the draft in order to have the most optimal
lineup.

I set up an interview with my end user relating to the topic and the
responses will be shown below:

1.  **What is your name?**

    Aaron Sutcliffe

2.  **Do you use any external resources to create fantasy line-ups?**

    No

3.  **What would you like to see in a hypothetical draft/line-up
    optimiser?**

    I want a compact method of analysing what players I can use for my
    drafts. I would also like to compare player stats to manually judge
    which player would be a good fit for my draft. I would also like a
    way to save and export lineups in its file formats (JSON or CSV)

4.  **From highest to lowest, rank the importance of certain features in
    most draft optimisers**

- Stats

- Predicted points per game

- Player details

- 'Sleeper' picks

- Expert analysis

5.  **Are there any other features you'd like you see in a draft
    optimiser?**\
    An easy way to highlight players to make them stand out in a clear
    and concise way

Furthermore, I created a survey and asked my end user along with a few
other basketball fantasy managers to take part and I have added the
results below:\
![](media/image1.png){width="6.268055555555556in" height="3.4625in"}

![](media/image2.png){width="6.268055555555556in"
height="3.453472222222222in"}

![](media/image3.png){width="6.268055555555556in"
height="1.0972222222222223in"}

![](media/image4.png){width="6.268055555555556in"
height="3.4194444444444443in"}

![](media/image5.png){width="6.268055555555556in" height="3.44375in"}

![](media/image6.png){width="6.268055555555556in" height="1.7125in"}

The problem that they found was that there was a lack of simple
interfaces for fantasy sport optimisers; most casual players would often
feel overwhelmed by the complicated features of draft optimisers and the
unnecessary stats that are added. The market for draft optimisers is
also very saturated, so a product that simplifies the process could end
up being very useful. They would like to see if a simpler interface
could generate better results for users than a complicated interface
that forces the user to do most of the work themselves.

## Current System

Currently Aaron plans his drafts through two methods:

- Personal knowledge -- He is an avid fan of the NBA, so he has
  knowledge of player performance to a certain extent. This allows him
  to create lineups based on his knowledge as well as based on his
  personal interests -- such as creating lineups with his favourite
  players or players from his favourite team

- Social media and News -- Aaron follows a lot of fantasy draft social
  media accounts that provide him with daily and weekly updates on
  player progression and points. There are also NBA fantasy news sites
  that provide him with updates with professional analysis on player
  performance

Aaron also uses ESPN fantasy to make his online drafts so I will be
using its drafting process to describe the current system.

He then joins a fantasy league by filtering through his personal
requirements such as league difficulty (beginner leagues or expert),
scoring type (H2H, Season points, etc) and draft system. Once in a
league that suits his requirements, he is allowed to select a list of
players he would like to save in advance. While this does not guarantee
he will be able to select these players it speeds up the process of
searching for them in the list of NBA players.

Once the draft process starts, the managers in the league get a random
draft pick each round. Then the manager with the first pick selects the
player they would like on their team. Once the player is selected, the
draft provides a chance for the manager to auction the card to the other
managers in order to improve their salary while providing the other
manager with a better player. When it is Aaron's turn, he selects a
player from the list and adds them to his lineup. If there are any
players from his list of saved players, he can have the choice to add
them to the team automatically as long as it fits within the positional
constraints. This process repeats for each round until every manager has
a full lineup of players.

After the draft process, the managers also have the choice to buy and
sell their players as well as swap players in their lineups for ones
that hadn't been selected. This means that Aaron would be able to change
his lineup on a weekly basis based on how each player performs.

## Current Solutions

In order to research for my project, I've looked at examples of existing
lineup optimisers that are present in most online fantasy basketball
leagues such as yahoo and draftpicks. What I have found is that there
are already solutions for the problem such as expert rankings, draft
kits and built-in auto-pick features on fantasy platforms. Users could
also build their own spreadsheets or follow live blogs, but these
methods are manual and often very difficult and takes a long time, which
most casual fantasy managers would want to avoid.

![A screenshot of a computer AI-generated content may be
incorrect.](media/image7.png){width="5.383333333333334in"
height="5.2in"}

(Example of a detailed draft analysis chart with players ranked on
fantasy points and other stats)

![A screenshot of a video game AI-generated content may be
incorrect.](media/image8.png){width="5.641666666666667in"
height="5.316666666666666in"}

(expert analysis on future league rankings)

> ![A screenshot of a sports app AI-generated content may be
> incorrect.](media/image9.png){width="4.816666666666666in"
> height="5.008333333333334in"}

# Requirements

1.  Lineups

    1.  The program must have at least one or more lineups that fully
        comply to the end users' requirements

        1.  Every lineup must contain the same number of players and
            must contain the correct number of player positions for each
            team

        2.  The lineup must include any certain players selected by the
            user and exclude certain players selected as well

        3.  Lineups must include every player's NBA ID if chosen by the
            user

        4.  Lineups should be extractable in JSON form (Optional - Could
            also allow CSV however JSON is the more common format)

    2.  The user should be able to change the lineup in real time based
        on any current injuries or if the players have been drafted by
        other teams

2.  Players

    1.  The program should contain enough information on players to
        allow the end user to have a thorough understanding of each
        players stat

    2.  The system should be able to consider players that play more
        than one position (PG who also play SG etc)

    3.  The end user should also be given a predicted points for each
        player as well as predicting the points from the entire lineup

    4.  Optional - The program could factor in variance/volatility of
        players to give the end user a deeper understanding of how
        certain players may garner points in a week

3.  System

    1.  Login:

        1.  There should be a way for the user to login to access the
            system

        2.  The login system should contain a format for each password
            (must contain a capital letter, one symbol and must contain
            a minimum number of characters

        3.  Once user logs in, their login info should be stored to be
            used to view their individual lineups

    2.  UI:

        1.  Must be clear and concise with proper labels and buttons

        2.  UI should direct user to the correct parts of the program

        3.  UI should follow a similar format to keep it organised

        4.  The UI section of the program must be written in OOP in
            order to improve code organization

    3.  Optimiser:

        1.  The program must run based on the mathematical formula used
            to maximise points based on position, predicted points per
            game and teams.

        2.  It must use all the players in the player list

        3.  Every lineup should be unique from each other for each
            instance of the optimiser being run

        4.  The optimiser should use an appropriate file format

    4.  API:

        1.  The application must have a link to the NBA API

        2.  The API should provide updated and correct information to
            the user

        3.  The player list generated by the API should follow the same
            format for every instance

# Design

## External resources

To create my project, I will need to use the following external packages
in python:

- PuLP optimiser to perform mathematical operations.

  - PuLP is especially useful in order to calculate total points scored
    by a player as well as any roster constraint such as player
    positions.

  - It would use all this information in order to create the most
    optimal lineup for you based on your requirements.

<!-- -->

- Pandas to create and manipulate data structures.

  - It would store all player data in a table and alter availability as
    players are drafted.

  - It would also work with other optimisation programs in order to
    manage lineups based on other constraints

  - It would also be used to create a list of all possible lineups based
    on the requirements or changes.

<!-- -->

- OpenPyXL to read and write into Excel spreadsheets.

  - This will be used to read through existing player spreadsheets and
    use the information present in them.

  - It saves time for me as I would not need to copy the information of
    the spreadsheet into a text file in order to read through it.

  - Furthermore, almost all NBA player data is stored on excel
    spreadsheets, so this extension is important

<!-- -->

- RegEx to create search patterns

  - This would be used to clean up data in order to only get the
    required information (Ex: Getting rid of middle names of players or
    only using initials and last name to make data more compact to view)

  - It would also be used for user input validation to make sure users
    only get results from the correct inputs

- PyQt5 to build my UI

  - PyQt5 is a simple, compact UI library that would be most optimal for
    my system as it doesn't require a complex UI to run.

  - PyQt5 also contains a designer that allows me to build windows using
    a graphical interface while allows for easier development of windows

- SQLite to perform SQL searches

  - I will be using SQLite to create and search through databases for
    sections such as the login system

- Hashlib to stored passwords securely

  - Allows me to hash passwords during the login and register section
    and store passwords in the database safely

- CSV/JSON to read/write files

  - Allows me to read CSV files to display tables etc and write CSV and
    JSON files for users to export their own lineups

## User Interface

I have created a set of diagrams in order to show how the interface is
meant to look like. In the diagrams you will also find annotations to
help understand each part of it. I plan on using PyQt5 to build this UI

(i) Menu Screen

    This will be the window that opens as soon as you open the
    application. The user is given two choices, to look at a player
    chart containing some data of the players or to access the lineup
    builder in order to start creating or optimising lineups

Takes the user to the Settings screen for the lineup

![Takes the user to the player chart
screen](media/image10.png){alt="A screenshot of a computer AI-generated content may be incorrect."
width="3.991304680664917in" height="3.980249343832021in"}

(ii) Player chart

     This window contains some simple player details that the fantasy
     user could use in order to gain information about a certain player.
     This window could be used if the user chooses to make any changes
     to their lineup themselves.

     This window works by the program initially converting a CSV file
     stored on the application into an XLSX file. It then separates the
     data into its individual headings, which turn into the headings for
     the treeview table.

Search bar to help user search for a specific player

![Shows the API number of the respective players if users would want to
import from the
spreadsheet](media/image11.png){width="6.260416666666667in"
height="2.1458333333333335in"}

Player details -- would include team and player stats

Predicted Fantasy points per game calculated using the formula

Player position

Full name of the player

(iii) Settings screen for rules of the league

      This window allows the user to input their league settings in
      order to generate accurate lineups. They can select the number of
      lineups they would want, the minimum and maximum total salary for
      the lineup, how many players they would like in each position and
      would also be able to filter out players in case they had already
      been selected.

Allows the user to pick a set number of lineups

Filter allows user to prevent certain players from being a part of the
lineup -- this section may be expanded to also give the user a chance to
guarantee some players a spot on the lineup

![User can also choose how many players they would want in each position
-- this section may contain some boundaries so users can't select an
exceeding number of players from a position or pick no players from a
certain position](media/image12.png){width="5.552858705161855in"
height="3.4171434820647417in"}

(iv) Lineups screen

     This screen gives the users a list of the best possible lineups
     they can choose. Within this they have the choice to save, edit and
     delete certain lineups. Currently there would be a fixed number of
     players per lineup but based on future requirements this could be
     updated to allow the user to

Names summarised to initial and last name to conserve space

Player positions

Allows user to delete certain lineups

Refreshes all the lineups with the new settings

Takes user back to edit the lineup settings

![Allows user to save the lineups into an excel
file](media/image13.png){width="6.260416666666667in"
height="2.7604166666666665in"}

Total team predicted points per game -- adds up all player PPG and
divides by number of players

# Process

## Mathematical Formula

In order for the draft optimiser to work optimally it would require the
following data:

- Player data: Includes player name, position, predicted points and
  salary

- Constraints: Salary cap, roster size, number of players per position

In order to find the predicted points for each player we would use the
normal model of fantasy points calculation which is:

- Points = 1.0 fantasy point

- Rebounds = 1.2 fantasy points

- Assists = 1.5 fantasy points

- Steals = 3.0 fantasy points

- Blocks = 3.0 fantasy points

- Turnovers = -1.0 fantasy points

The total points would then be calculated as:

FP = PTS + (1.2 \* REB) + (1.5 \* AST) + (3 \* STL) + (3 \* BLK) -- TOV

The mathematical formula used in this program is separated for the
maximum projected points per lineup and for position/salary constraints

- The maximum projected fantasy points are calculated using the formula:

$$\max\sum_{i}^{}{x_{i}p_{i}}$$

Where:

​$p_{i}$ = projected fantasy points for player i

$x_{i}$ = 1 if player is selected in the lineup or 0 if player is not
selected

- The positional constraint is calculated using the formula:

$$\sum_{i}^{}{pos(i,j)*x_{i} = R_{j}}$$

Where:

$pos(i,j)$= 1 if player is eligible for the position or 0 if player is
not

$R_{j}$= required number of players for position j

## Optimiser

The optimiser uses the mathematical formula in order to select the best
set of players based on player and positional constraints

It does this through the following steps:

1.  Validation check -- the program first checks if the number of
    lineups as well as number of players in each position are selected

2.  Data preparation -- The program loads the CSV file and expands
    multiposition players into two separate rows. It then creates an
    excel workbook in order to temporarily store the data and creates
    the column headers matching the player table

3.  Optimisation preparation -- The program extracts the required
    headers from the CSV and creates a points dictionary for each player
    based on position with their NBA ID and position. This makes it
    easier to search for a player during the optimisation process. A
    dictionary for the positional constraints is also made

4.  Optimisation loop

    a.  Initialise the loop -- The program creates an empty loop and
        loops through for the number of lineups selected

    b.  Binary variables -- The program creates binary variables for
        each player at each position where 1 = player is selected and 0
        = player is not selected

    c.  Create and define -- The program creates the optimisation
        problem through PuLP with the goal to maximise total fantasy
        points. The objective function is also built to maximise the sum
        of (player_points \* binary variable) to calculate the sum of
        the selected player in each instance

    d.  Add position constraints -- Makes sure guard, forward and center
        variables equal the corresponding number of guard, forward and
        center values provided

    e.  Add unique player constraints -- The program makes sure each
        player is only selected at one position at a time by checking if
        the sum of all variables of a player across all positions is
        \<=1

    f.  Add include/exclude player constraints -- The program then
        forces certain players who are selected by the user to be in
        each lineup. The player is found by comparing the selected
        player's NBA ID (which is extracted from the filter table) with
        the dictionary to find the corresponding player. The program
        also makes sure these players are only selected in one position.
        The excluding process works in the same way by setting their
        variable to 0

    g.  Add uniqueness constraint to each lineup -- The program then
        compares the new lineup to the previous one to make sure each
        instance is different by at least one player. On the first
        instance the lineup is instead just saved to the list of
        previous lineups later in the program

    h.  Solve -- The program then solves the optimisation problem

5.  Extract selected players -- The program checks which players have
    the value of 1 and retrieves the player names and points and
    organises them by position. The program then calculates the total
    fantasy points for the lineup

6.  Write lineup to Excel -- The program then writes each lineup into an
    excel spreadsheet and is formatted with the total score added at the
    end column

7.  Save and open -- The excel workbook is saved and is opened through
    the OptimisedTable function

[Pseudocode]{.underline}

// Organize player points by position

points ← {}

FOR EACH pos IN available_positions

points\[pos\] ← PlayerID, points // Creates a dictionary of playerID and
position

ENDFOR

// Set position requirements

pos_num_available ← {\"PG\": 2, \"SG\": 2, \"SF\": 2, \"PF\": 2, \"C\":
1}

previous_lineups ← \[\] // Makes an empty array to only store
information of the previous lineup

// Generate unique lineups based on how many user needs

FOR lineup ← 1 TO number_lineups

// Create binary decision variables for each player

\_vars ← create binary variables for each position and player

// Create optimization problem to maximize points

prob ← new LpProblem(maximize)

// Point maximising objective

prob.ADD_OBJECTIVE(sum of all player_points \*
\_vars\[pos\]\[player_id\])

// Positional constraints

FOR EACH pos IN positions

prob.ADD_CONSTRAINT(sum of \_vars\[pos\] = pos_num_available\[pos\])

ENDFOR

// Creates unique lineup

FOR EACH prev_lineup IN previous_lineups

prob.ADD_CONSTRAINT(overlap with prev_lineup ≤ lineup_size - 1)

ENDFOR

prob.solve()

IF no solution found THEN

BREAK

ENDIF

// Extract selected players where variable = 1

selected_players ← \[\]

FOR EACH pos, player_id IN all combinations

IF \_vars\[pos\]\[player_id\] = 1 THEN

selected_players.APPEND((pos, player_id))

ENDIF

ENDFOR

// Adds the created lineup into previous lineup to use for comparison

previous_lineups.APPEND(selected_players)

ENDFOR

## API

The player data is retrieved through the official NBA API and is stored
in a CSV file. The data is enriched with the player position as well as
player statistics required to calculate total fantasy points along with
other informative data such as full name and team. The process used to
generate the player table can be observed through the following data
flow diagram.

![](media/image14.png){width="5.239328521434821in"
height="6.083333333333333in"}

## Object Oriented Programming

For the program OOP is used primarily within the frontend section of the
code in order to add organisation and flexibility into the code while
keeping it easy to maintain compared to the procedural method of coding.

In OOP the UI and its and its parts are encapsulated within classes and
objects which removes the need for global variables which makes
debugging much easier and makes code more readable.

This also allows for code to be reused throughout the application. For
example, the front end of the register and login pages are almost
identical so reusing code from one of these for the other simplifies the
coding process. Additionally, inheritance within OOP allows for
subclasses that improve the debugging process.

## Database

The program uses a database in order to store user information

[User information]{.underline}

Users are required to sign up and login in order to use the program.
This data is stored within a database file using SqLite3. The data is
used in order to:

- Create Security -- Prevents unknown users from accessing the device

- Improve User Experience -- Allows users to store their individual
  lineups, access them and export them within the application

CREATE TABLE User (

UserID int(25) PRIMARY KEY,

Username varchar(255),

Password varchar(255)

);

The data is saved in the table in the following structure:

Each user's data is stored with a user ID as the primary key. This user
ID is then linked to each lineup that is saved. This means that each
lineup can only be viewed by the account that created it.

The password is also hashed using hashlib in order to keep data more
secure from vulnerability leaks. Once hashed the program hashes the
password entry during the login stage and compares it to the original
hashed password

[Player Information]{.underline}

Data such as player information and stats will be extracted from the NBA
API which would be opened in CSV format which would be parsed and
inserted into its respective tables, which allows the data to be changed
constantly depending on how often the user updates the data

Users would also be able to directly extract the lineups into the
software that they use for their fantasy leagues as most leagues allow
lineups to be imported in the CSV format.

## File Storage

- The program will also contain file storage features such as allowing
  the user to save their login information onto a database file to
  access their individual program.

<!-- -->

- In order to save time, the program also creates a copy of the player
  list extracted by the NBA API. This can be updated with the click of a
  button, however extracting a large dataset takes a very long time so
  storing it within the application speeds up the process.

- They can also choose to save their lineups and export it in .txt or
  JSON format to be able to directly import it into their fantasy
  websites.

## Player Table/Filter Table/Optimised Table

All three tables use similar structure to generate the table to use as
well as to search within the data. This information can be shown as a
flowchart describing the processes required to load the data

After the data is loaded, specific players, teams or positions can be
searched using the search_table() function which simply strips case
sensitivity and unnecessary spaces before comparing the search data with
all data in the row and column. If there is a match, then all other rows
except for matched rows are hidden. The data is then restored through
the clear_search() function which makes all rows visible

![](media/image15.png){width="5.354166666666667in"
height="9.549381014873141in"}

[IPSO chart]{.underline}

+----------------------------------+-----------------------------------+
| [Inputs]{.underline}             | [Outputs]{.underline}             |
|                                  |                                   |
| - Username and password          | - Lineup rules window             |
|                                  |                                   |
| - Number of lineups              | - Created lineups                 |
|                                  |                                   |
| - Number of players and          | - Player details from NBA API     |
|   positions per lineup           |                                   |
|                                  |                                   |
| - Player name in search bar      |                                   |
+==================================+===================================+
| [Processes]{.underline}          | [Storage]{.underline}             |
|                                  |                                   |
| - Authenticate username and      | - Player list                     |
|   password                       |                                   |
|                                  | - Saved Lineups                   |
| - Search for players within      |                                   |
|   spreadsheet                    | - Login details                   |
|                                  |                                   |
| - Generate lineups using rules   |                                   |
|   and mathematical formula       |                                   |
|                                  |                                   |
| - Save lineups to file           |                                   |
|                                  |                                   |
| - Updating data using NBA API    |                                   |
+----------------------------------+-----------------------------------+

# Technical Solution

## Login

![](media/image16.emf)

## Register

![](media/image17.emf)

## Optimised Table

### Loading Data

![](media/image18.emf)

### Search Table

![](media/image19.emf)

[]{#_Toc221568563 .anchor}CSV/JSON Saving![](media/image20.emf)

![](media/image21.emf)

## 

## 

## 

## Update Player List

![](media/image22.emf)

                               

                                ![](media/image23.emf)  

![](media/image24.emf)               

                ![](media/image25.emf)

## Optimiser

![](media/image26.emf)     ![](media/image27.emf)

                                ![](media/image28.emf)

       

![](media/image29.emf)

![](media/image30.emf)![](media/image31.emf)

# Testing

Link to the testing video: https://youtu.be/8WFb3ELPLrE

+-------+-------------------+------------------------+-------------+-------------+
| Test  | Test summary      | Test Type              | Intended    | Video       |
| ID    |                   |                        | response    | timestamp   |
+=======+===================+========================+=============+=============+
| 1.1   | Login to the      | Function test          | User can    | 0:00        |
|       | program           |                        | log in      |             |
+-------+-------------------+------------------------+-------------+-------------+
| 1.1.1 | Attempt to login  | Validation test        | Error       | 0:07        |
|       | with a            |                        | message     |             |
|       | non-existing      |                        | appears     |             |
|       | username and      |                        |             |             |
|       | password          |                        |             |             |
+-------+-------------------+------------------------+-------------+-------------+
| 1.1.2 | Login with an     | Validation test        | User logs   | 0:57        |
|       | existing username |                        | in          |             |
|       | and password      |                        |             |             |
+-------+-------------------+------------------------+-------------+-------------+
| 1.2   | Register a new    | Function test          | User can    | 0:19        |
|       | account           |                        | register an |             |
|       |                   |                        | account     |             |
+-------+-------------------+------------------------+-------------+-------------+
| 1.2.1 | Attempt to create | Security/Validation    | Error       | 0:24        |
|       | an account with   | test                   | message     |             |
|       | user "abc" and    |                        | appears     |             |
|       | password "123"    |                        |             |             |
+-------+-------------------+------------------------+-------------+-------------+
| 1.2.2 | Attempt to create | Validation test        | User        | 0:40        |
|       | an account with   |                        | registers   |             |
|       | username          |                        | account     |             |
|       | "Guest@2026" and  |                        |             |             |
|       | password"         |                        |             |             |
|       | HelloWorld@2026"  |                        |             |             |
+-------+-------------------+------------------------+-------------+-------------+
| 1.3   | Show that         | Security test          | Passwords   | 1:32        |
|       | passwords are     |                        | are         |             |
|       | hashed in the     |                        | properly    |             |
|       | database          |                        | hashed      |             |
+-------+-------------------+------------------------+-------------+-------------+
| 2.1   | View all windows  | UI test                | All windows | 1:43        |
|       | in the            |                        | must have   |             |
|       | application       |                        | clear       |             |
|       |                   |                        | labels and  |             |
|       |                   |                        | buttons     |             |
+-------+-------------------+------------------------+-------------+-------------+
| 2.2   | Switch from one   | UI test                | Buttons     | 1:53        |
|       | window to the     |                        | should      |             |
|       | other using       |                        | allow users |             |
|       | buttons           |                        | to switch   |             |
|       |                   |                        | between     |             |
|       |                   |                        | windows     |             |
+-------+-------------------+------------------------+-------------+-------------+
| 3.1   | Open player table | Data Validation test   | CSV data    | 2:13        |
|       | and show that it  |                        | matches     |             |
|       | is the same as    |                        | player      |             |
|       | the CSV file      |                        | table       |             |
+-------+-------------------+------------------------+-------------+-------------+
| 3.2.1 | Show a player     | Unit test              | Player is   | 2:58        |
|       | with multiple     |                        | listed with |             |
|       | positions         |                        | multiple    |             |
|       |                   |                        | positions   |             |
+-------+-------------------+------------------------+-------------+-------------+
| 3.2.2 | Search for player | Data Validation test   | Jalen       | 3:13        |
|       | "Jalen Johnson"   |                        | Johnson is  |             |
|       |                   |                        | the only    |             |
|       |                   |                        | player on   |             |
|       |                   |                        | the player  |             |
|       |                   |                        | table       |             |
+-------+-------------------+------------------------+-------------+-------------+
| 3.2.3 | Search for player | Data Validation test   | Nothing     | 3:25        |
|       | "Micheal Phelps"  |                        | appears on  |             |
|       |                   |                        | the player  |             |
|       |                   |                        | table       |             |
+-------+-------------------+------------------------+-------------+-------------+
| 3.2.4 | Search for the    | Data Validation test   | Every       | 3:42        |
|       | Guard position    |                        | player      |             |
|       |                   |                        | lister at   |             |
|       |                   |                        | the guard   |             |
|       |                   |                        | position    |             |
|       |                   |                        | appears     |             |
+-------+-------------------+------------------------+-------------+-------------+
| 4.1   | Create an         | Functional test        | Lineups     | 4:23        |
|       | optimized lineup  |                        | containing  |             |
|       | and show that it  |                        | best set of |             |
|       | exists            |                        | players     |             |
|       |                   |                        | given       |             |
|       |                   |                        | constraints |             |
|       |                   |                        | are created |             |
+-------+-------------------+------------------------+-------------+-------------+
| 4.1.1 | Create a lineup   | Functional test        | Lineups     | 4:09        |
|       | with 4 Guards, 4  |                        | with the    |             |
|       | Forwards and 2    |                        | positional  |             |
|       | Centers           |                        | constraints |             |
|       |                   |                        | is created  |             |
|       | Then reset the    |                        |             |             |
|       | optimiser and     |                        |             |             |
|       | create a lineup   |                        |             |             |
|       | with 2 Guards, 5  |                        |             |             |
|       | Forwards and 3    |                        |             |             |
|       | Centers           |                        |             |             |
+-------+-------------------+------------------------+-------------+-------------+
| 4.1.2 | In the filter     | Unit/Functional test   | Every       | 5:05        |
|       | search exclude    |                        | lineup will |             |
|       | the player Nikola |                        | exclude     |             |
|       | Jokic and include |                        | Jokic and   |             |
|       | the player Amen   |                        | include     |             |
|       | Thompson          |                        | Thompson    |             |
+-------+-------------------+------------------------+-------------+-------------+
| 4.1.3 | Create 5 lineups  | Functional test        | Number of   | 5:40        |
|       | with random       |                        | lineups     |             |
|       | settings then     |                        | will match  |             |
|       | create 10 with    |                        | selection   |             |
|       | the same settings |                        |             |             |
+-------+-------------------+------------------------+-------------+-------------+
| 4.2   | Update player     | Functional/Integration | The player  | 6:10        |
|       | list using API    | test                   | list will   |             |
|       | and create        |                        | be updated  |             |
|       | another optimised |                        | with most   |             |
|       | lineup            |                        | recent data |             |
+-------+-------------------+------------------------+-------------+-------------+
| 5.1   | Save lineup as    | Integration test       | CSV data    | 6:40        |
|       | CSV and show      |                        | will match  |             |
|       | saved location    |                        | lineups     |             |
+-------+-------------------+------------------------+-------------+-------------+
| 5.2   | Save lineup as    | Integration test       | JSON data   | 7:12        |
|       | JSON and show     |                        | will match  |             |
|       | saved location    |                        | linups      |             |
+-------+-------------------+------------------------+-------------+-------------+

# Evaluation

## Beta testing 

After completing my project, I am pleased with the final outcome and
believe that it matches most of my initial requirements. I have also
received information from my end user as well as other third parties who
play tested the program. Going through the data it can be concluded that
both my end user and third party would prefer to use my product over
other online sites.

![](media/image32.png){width="6.268055555555556in"
height="1.7381944444444444in"}

![](media/image33.png){width="6.268055555555556in"
height="3.4604166666666667in"}

![](media/image34.png){width="6.268055555555556in"
height="3.4590277777777776in"}

![](media/image35.png){width="6.268055555555556in"
height="3.442361111111111in"}

![](media/image36.png){width="6.268055555555556in"
height="3.4305555555555554in"}

![](media/image37.png){width="6.268055555555556in"
height="2.1798611111111112in"}

![](media/image38.png){width="6.268055555555556in"
height="3.432638888888889in"}

## Evaluation of requirements 

- Lineups

  - The program must have at least one or more lineups that fully comply
    to the end users' requirements - ACHIEVED

  - Every lineup must contain the same number of players and must
    contain the correct number of player positions for each team -
    ACHIEVED

  - The lineup must include any certain players selected by the user and
    exclude certain players selected as well - ACHIEVED

  - Lineups must include every player's NBA ID if chosen by the user -
    PARTIALLY ACHIEVED

  - Lineups should be extractable in JSON form (Optional - Could also
    allow CSV however JSON is the more common format) - ACHIEVED

  - The user should be able to change the lineup in real time based on
    any current injuries or if the players have been drafted by other
    teams -- PARTIALLY ACHIEVED (Players ca make real time changes but
    it has to be done manually)

- Players

- The program should contain enough information on players to allow the
  end user to have a thorough understanding of each players stat -
  ACHIEVED

- The system should be able to consider players that play more than one
  position (PG who also play SG etc) - ACHIEVED

- The end user should also be given predicted points for each player as
  well as predicting the points from the entire lineup- ACHIEVED

- Optional - The program could factor in variance/volatility of players
  to give the end user a deeper understanding of how certain players may
  garner points in a week -- NOT ACHIEVED (Would require further
  prediction models to achieve)

- System

  - Login:

    - There should be a way for the user to login to access the system -
      ACHIEVED

    - The login system should contain a format for each password (must
      contain a capital letter, one symbol and must contain a minimum
      number of characters- ACHIEVED

    - Once user logs in, their login info could be stored to be used to
      view their individual lineups - NOT ACHIEVED

  - UI:

    - Must be clear and concise with proper labels and buttons -
      ACHIEVED

    - UI should direct user to the correct parts of the program -
      ACHIEVED

    - UI should follow a similar format to keep it organised - ACHIEVED

    - The UI section of the program must be written in OOP in order to
      improve code organization - ACHIEVED

  - Optimiser:

    - The program must run based on the mathematical formula used to
      maximise points based on position, predicted points per game and
      teams - ACHIEVED

    - It must use all the players in the player list - ACHIEVED

    - Every lineup should be unique from each other for each instance of
      the optimiser being run - ACHIEVED

    - The optimiser should use an appropriate file format - ACHIEVED

  - API:

    - The application must have a link to the NBA API - ACHIEVED

    - The API should provide updated and correct information to the
      user - ACHIEVED

    - The player list generated by the API should follow the same format
      for every instance - ACHIEVED

## Conclusion

Using the PuLP optimiser rather than building my own minimax proved to
be useful as it provided me with linear optimisation skills that I could
use in the future. However, I would like to come back to this project
and attempt to build the optimiser through a different model.

I also struggled to find quality documentation in order to build proper
fetch requests from the NBA API which resulted in that section feeling
extremely complicated and bloated. If I was able to revisit that
section, I would definitely remodel it to be more optimised.

One feature that I hoped to add was linking Player data to lineups built
by the player as that would make the login system more useful rather
than just being a gateway to the app. However, I struggled to find
documentation that could guide me to building such a feature

Another feature that I would change would be the file handling for the
project. It would have been better if I had created a database for the
player rather than use a CSV file however I had planned to give users
the option to insert their own player lists into the system however that
would cause formatting and security issues, so I decided against it.
Therefore, implementing a database would have been the better option.

In conclusion I believe that my program provides users with a more
streamlined option to create optimised lineups to be used in the future
and reaches the requirements by my end user as well as the requirements
that I set onto the program.

# Appendix

## Source code

### Login

1 \| import hashlib

2 \| from PyQt5 import QtCore, QtGui, QtWidgets

3 \| from MainWindow import Ui_MainScreen

4 \| from Register import Ui_RegisterScreen

5 \| import sqlite3

6 \| ​

7 \| class Ui_MainWindow(object):

8 \|     

9 \|     def LoginAccount(self):

10\| ​

11\|         def existing_user_error():

12\|                 error_dialog = QtWidgets.QErrorMessage()

13\|                 error_dialog.showMessage(\'Username already
exists.\')

14\|                 error_dialog.exec\_()

15\| ​

16\|         def login_error():

17\|                 error_dialog = QtWidgets.QErrorMessage()

18\|                 error_dialog.showMessage(\'Login Failed. Please
check your username and password.\')

19\|                 error_dialog.exec\_()

20\| ​

21\|         def login_success():

22\|                 sucess_dialog = QtWidgets.QMessageBox()

23\|                 sucess_dialog.setText(\'Login Successful!\')

24\|                 sucess_dialog.exec\_()

25\| ​

26\|         def login_database():

27\|            try:

28\|                 conn = sqlite3.connect(\"login.db\") \# accesses
the database

29\|                 cur = conn.cursor()

30\| ​

31\|                 entered_password_hash =
hashlib.sha256(self.PasswordEntry.text().encode()).hexdigest()

32\| ​

33\|                 cur.execute(\"SELECT \* FROM login WHERE username
=? AND password=?\", (self.UsernameEntry.text(), entered_password_hash))
#searches for the username and password entered

34\|                 row =cur.fetchall() \# finds the example of
username and password

35\|                 if row !=\[\]:

36\|                         user_name = row\[0\]\[0\]

37\|                         login_success()

38\|                         self.window = QtWidgets.QMainWindow()

39\|                         self.ui = Ui_MainScreen()

40\|                         self.ui.setupUi(self.window)

41\|                         self.window.show()

42\|                 else:

43\|                       login_error()

44\|                       

45\|            except Exception as e:

46\|                 print(f\"Error: {e}\")

47\|         login_database()

48\| ​

49\|     def RegisterAccount(self):

50\|         self.window = QtWidgets.QMainWindow()

51\|         self.ui = Ui_RegisterScreen()

52\|         self.ui.setupUi(self.window)

53\|         self.window.show()

54\| ​

55\|     def setupUi(self, MainWindow):

56\|         MainWindow.setObjectName(\"LoginWindow\")

57\|         MainWindow.resize(577, 600)

58\|         MainWindow.setStyleSheet(\"background-color: rgb(81, 81,
81)\")

59\|         self.centralwidget = QtWidgets.QWidget(MainWindow)

60\|         self.centralwidget.setObjectName(\"centralwidget\")

61\|         self.LoginLabel = QtWidgets.QLabel(self.centralwidget)

62\|         self.LoginLabel.setGeometry(QtCore.QRect(240, 40, 121, 71))

63\|         self.LoginLabel.setStyleSheet(\"font: 28pt \\\"MS Shell Dlg
2\\\";\\n\"

64\| \"color: rgb(255, 255, 255);\")

65\|         self.LoginLabel.setObjectName(\"LoginLabel\")

66\|         self.UsernameLabel = QtWidgets.QLabel(self.centralwidget)

67\|         self.UsernameLabel.setGeometry(QtCore.QRect(50, 170, 91,
31))

68\|         self.UsernameLabel.setStyleSheet(\"color: rgb(255, 255,
255);\\n\"

69\| \"font: 11pt \\\"MS Shell Dlg 2\\\";\")

70\|         self.UsernameLabel.setObjectName(\"UsernameLabel\")

71\|         self.UsernameEntry =
QtWidgets.QLineEdit(self.centralwidget)

72\|         self.UsernameEntry.setGeometry(QtCore.QRect(160, 170, 291,
41))

73\|         self.UsernameEntry.setStyleSheet(\"color: rgb(255, 255,
255);\\n\"

74\| \"font: 10pt \\\"MS Shell Dlg 2\\\";\")

75\|         self.UsernameEntry.setText(\"\")

76\|         self.UsernameEntry.setObjectName(\"UsernameEntry\")

77\|         self.PasswordEntry =
QtWidgets.QLineEdit(self.centralwidget)

78\|       
 self.PasswordEntry.setEchoMode(QtWidgets.QLineEdit.Password)

79\|         self.PasswordEntry.setGeometry(QtCore.QRect(160, 250, 291,
41))

80\|         self.PasswordEntry.setStyleSheet(\"color: rgb(255, 255,
255);\\n\"

81\| \"font: 10pt \\\"MS Shell Dlg 2\\\";\")

82\|         self.PasswordEntry.setText(\"\")

83\|         self.PasswordEntry.setObjectName(\"PasswordEntry\")

84\|         self.PasswordLabel = QtWidgets.QLabel(self.centralwidget)

85\|         self.PasswordLabel.setGeometry(QtCore.QRect(50, 250, 80,
31))

86\|         self.PasswordLabel.setStyleSheet(\"color: rgb(255, 255,
255);\\n\"

87\| \"font: 11pt \\\"MS Shell Dlg 2\\\";\")

88\|         self.PasswordLabel.setObjectName(\"PasswordLabel\")

89\|         self.LoginButton =
QtWidgets.QPushButton(self.centralwidget, clicked = lambda:
self.LoginAccount())

90\|         self.LoginButton.setGeometry(QtCore.QRect(300, 370, 151,
41))

91\|         self.LoginButton.setStyleSheet(\"background-color: rgb(195,
195, 195);\\n\"

92\| \"font: 9pt \\\"MS Shell Dlg 2\\\";\")

93\|         self.LoginButton.setObjectName(\"LoginButton\")

94\|         self.CreateAccount =
QtWidgets.QPushButton(self.centralwidget, clicked = lambda:
self.RegisterAccount())

95\|         self.CreateAccount.setGeometry(QtCore.QRect(300, 320, 151,
21))

96\|         self.CreateAccount.setStyleSheet(\"background-color:
rgb(195, 195, 195);\\n\"

97\| \"font: 9pt \\\"MS Shell Dlg 2\\\";\")

98\|         self.CreateAccount.setObjectName(\"CreateAccount\")

99\|         MainWindow.setCentralWidget(self.centralwidget)

100\|         self.menubar = QtWidgets.QMenuBar(MainWindow)

101\|         self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 21))

102\|         self.menubar.setObjectName(\"menubar\")

103\|         MainWindow.setMenuBar(self.menubar)

104\|         self.statusbar = QtWidgets.QStatusBar(MainWindow)

105\|         self.statusbar.setObjectName(\"statusbar\")

106\|         MainWindow.setStatusBar(self.statusbar)

107\| ​

108\|         self.retranslateUi(MainWindow)

109\|         QtCore.QMetaObject.connectSlotsByName(MainWindow)

110\| ​

111\|     def retranslateUi(self, MainWindow):

112\|         \_translate = QtCore.QCoreApplication.translate

113\|         MainWindow.setWindowTitle(\_translate(\"MainWindow\",
\"MainWindow\"))

114\|         self.LoginLabel.setText(\_translate(\"MainWindow\",
\"Login\"))

115\|         self.UsernameLabel.setText(\_translate(\"MainWindow\",
\"Username\"))

116\|         self.PasswordLabel.setText(\_translate(\"MainWindow\",
\"Password\"))

117\|         self.LoginButton.setText(\_translate(\"MainWindow\",
\"Login\"))

118\|         self.CreateAccount.setText(\_translate(\"MainWindow\",
\"Create Account\"))

119\| ​

120\| ​

121\| if \_\_name\_\_ == \"\_\_main\_\_\":

122\|     import sys

123\|     app = QtWidgets.QApplication(sys.argv)

124\|     MainWindow = QtWidgets.QMainWindow()

125\|     ui = Ui_MainWindow()

126\|     ui.setupUi(MainWindow)

127\|     MainWindow.show()

128\|     sys.exit(app.exec\_())

### Register

1 \| 1 \| import hashlib

2 \| 2 \| from PyQt5 import QtCore, QtGui, QtWidgets

3 \| 3 \| import sqlite3

4 \| 4 \| import re

5 \| 5 \| •

6 \| 6 \| •

7 \| 7 \| class Ui_RegisterScreen(object):

8 \| 8 \|     def existing_user_error(self):

9 \| 9 \|         error_dialog = QtWidgets.QErrorMessage()

10\| 10\|         error_dialog.showMessage(\'Username already exists.\')

11\| 11\|         error_dialog.exec\_()

12\| 12\| •

13\| 13\|     def register_success(self):

14\| 14\|                 sucess_dialog = QtWidgets.QMessageBox()

15\| 15\|                 sucess_dialog.setText(\'Register
Successful!\')

16\| 16\|                 sucess_dialog.exec\_()

17\| 17\| •

18\| 18\|     def register_database(self):

19\| 19\|             conn = sqlite3.connect(\"login.db\") \# accesses
the database

20\| 20\|             cur = conn.cursor()

21\| 21\|             cur.execute(\"CREATE TABLE IF NOT EXISTS login
(username TEXT PRIMARY KEY, password TEXT)\")

22\| 22\|            

23\| 23\|             try:

24\| 24\|                  def username_validation():

25\| 25\|                      username = self.UsernameEntry.text()

26\| 26\|                      pattern =
r\"\^(?=.\*\[a-z\])(?=.\*\[A-Z\])(?=.\*\\d)(?=.\*\[!@#\$%\^&\*()-+\]).{5,20}\$\"

27\| 27\| •

28\| 28\|                      if not re.match(pattern, username):

29\| 29\|                          username_error =
QtWidgets.QErrorMessage()

30\| 30\|                          username_error.showMessage(\'Username
must be 8-20 characters long and include at least one uppercase letter,
one lowercase letter, one digit, and one special character
(!@#\$%\^&\*()-+). \')

31\| 31\|                          username_error.exec\_()

32\| 32\| •

33\| 33\|                          return False

34\| 34\|                      else:

35\| 35\|                          return True

36\| 36\| •

37\| 37\|                  def password_validation():

38\| 38\|                      password = self.PasswordEntry.text()

39\| 39\|                      pattern =
r\"\^(?=.\*\[a-z\])(?=.\*\[A-Z\])(?=.\*\\d)(?=.\*\[!@#\$%\^&\*()-+\]).{5,20}\$\"

40\| 40\| •

41\| 41\|                      if not re.match(pattern, password):

42\| 42\|                          password_error =
QtWidgets.QErrorMessage()

43\| 43\|                          password_error.showMessage(\'Password
must be 8-20 characters long and include at least one uppercase letter,
one lowercase letter, one digit, and one special character
(!@#\$%\^&\*()-+).\')

44\| 44\|                          password_error.exec\_()

45\| 45\| •

46\| 46\|                          return False

47\| 47\|                      else:

48\| 48\|                          return True

49\| 49\| •

50\| 50\|                  if not username_validation() or not
password_validation():

51\| 51\|                      return

52\| 52\| •

53\| 53\|                  username_validation()

54\| 54\|                  password_validation()

55\| 55\| •

56\| 56\|                  password_hash =
hashlib.sha256(self.PasswordEntry.text().encode()).hexdigest()

57\| 57\|                  cur.execute(\"INSERT INTO login (username,
password) VALUES (?, ?)\", (self.UsernameEntry.text(), password_hash))
#inserts the username and password entered

58\| 58\|                  conn.commit()

59\| 59\|                  self.register_success()

60\| 60\| •

61\| 61\|             except sqlite3.IntegrityError:

62\| 62\|                 self.existing_user_error()

63\| 63\| •

64\| 64\|     def setupUi(self, RegisterScreen):

65\| 65\|         RegisterScreen.setObjectName(\"RegisterScreen\")

66\| 66\|         RegisterScreen.resize(577, 600)

67\| 67\|         RegisterScreen.setStyleSheet(\"background-color:
rgb(81, 81, 81)\")

68\| 68\|         self.centralwidget = QtWidgets.QWidget(RegisterScreen)

69\| 69\|         self.centralwidget.setObjectName(\"centralwidget\")

70\| 70\|         self.label = QtWidgets.QLabel(self.centralwidget)

71\| 71\|         self.label.setGeometry(QtCore.QRect(200, 40, 181, 81))

72\| 72\|         self.label.setStyleSheet(\"font: 28pt \\\"MS Shell Dlg
2\\\";\\n\"

73\| 73\| \"color: rgb(255, 255, 255);\")

74\| 74\|         self.label.setObjectName(\"label\")

75\| 75\|         self.UsernameLabel =
QtWidgets.QLabel(self.centralwidget)

76\| 76\|         self.UsernameLabel.setGeometry(QtCore.QRect(50, 170,
91, 31))

77\| 77\|         self.UsernameLabel.setStyleSheet(\"color: rgb(255,
255, 255);\\n\"

78\| 78\| \"font: 11pt \\\"MS Shell Dlg 2\\\";\")

79\| 79\|         self.UsernameLabel.setObjectName(\"UsernameLabel\")

80\| 80\|         self.UsernameEntry =
QtWidgets.QLineEdit(self.centralwidget)

81\| 81\|         self.UsernameEntry.setGeometry(QtCore.QRect(160, 170,
291, 41))

82\| 82\|         self.UsernameEntry.setStyleSheet(\"color: rgb(255,
255, 255);\\n\"

83\| 83\| \"font: 10pt \\\"MS Shell Dlg 2\\\";\")

84\| 84\|         self.UsernameEntry.setText(\"\")

85\| 85\|         self.UsernameEntry.setObjectName(\"UsernameEntry\")

86\| 86\|         self.PasswordEntry =
QtWidgets.QLineEdit(self.centralwidget)

87\| 87\|        
self.PasswordEntry.setEchoMode(QtWidgets.QLineEdit.Password)

88\| 88\|         self.PasswordEntry.setGeometry(QtCore.QRect(160, 250,
291, 41))

89\| 89\|         self.PasswordEntry.setStyleSheet(\"color: rgb(255,
255, 255);\\n\"

90\| 90\| \"font: 10pt \\\"MS Shell Dlg 2\\\";\")

91\| 91\|         self.PasswordEntry.setText(\"\")

92\| 92\|         self.PasswordEntry.setObjectName(\"PasswordEntry\")

93\| 93\|         self.PasswordLabel =
QtWidgets.QLabel(self.centralwidget)

94\| 94\|         self.PasswordLabel.setGeometry(QtCore.QRect(50, 250,
80, 31))

95\| 95\|         self.PasswordLabel.setStyleSheet(\"color: rgb(255,
255, 255);\\n\"

96\| 96\| \"font: 11pt \\\"MS Shell Dlg 2\\\";\")

97\| 97\|         self.PasswordLabel.setObjectName(\"PasswordLabel\")

98\| 98\|         self.ResigterButton =
QtWidgets.QPushButton(self.centralwidget, clicked = lambda:
self.register_database())

99\| 99\|         self.ResigterButton.setGeometry(QtCore.QRect(300, 330,
151, 41))

100\| 100\|        
self.ResigterButton.setStyleSheet(\"background-color: rgb(195, 195,
195);\\n\"

101\| 101\| \"font: 9pt \\\"MS Shell Dlg 2\\\";\")

102\| 102\|        
self.ResigterButton.setObjectName(\"ResigterButton\")

103\| 103\|         RegisterScreen.setCentralWidget(self.centralwidget)

104\| 104\|         self.menubar = QtWidgets.QMenuBar(RegisterScreen)

105\| 105\|         self.menubar.setGeometry(QtCore.QRect(0, 0, 577,
26))

106\| 106\|         self.menubar.setObjectName(\"menubar\")

107\| 107\|         RegisterScreen.setMenuBar(self.menubar)

108\| 108\|         self.statusbar =
QtWidgets.QStatusBar(RegisterScreen)

109\| 109\|         self.statusbar.setObjectName(\"statusbar\")

110\| 110\|         RegisterScreen.setStatusBar(self.statusbar)

111\| 111\| •

112\| 112\|         self.retranslateUi(RegisterScreen)

113\| 113\|        
QtCore.QMetaObject.connectSlotsByName(RegisterScreen)

114\| 114\| •

115\| 115\|     def retranslateUi(self, RegisterScreen):

116\| 116\|         \_translate = QtCore.QCoreApplication.translate

117\| 117\|        
RegisterScreen.setWindowTitle(\_translate(\"RegisterScreen\",
\"MainWindow\"))

118\| 118\|         self.label.setText(\_translate(\"RegisterScreen\",
\"Register\"))

119\| 119\|        
self.UsernameLabel.setText(\_translate(\"RegisterScreen\",
\"Username\"))

120\| 120\|        
self.PasswordLabel.setText(\_translate(\"RegisterScreen\",
\"Password\"))

121\| 121\|        
self.ResigterButton.setText(\_translate(\"RegisterScreen\", \"Create
Account\"))

122\| 122\| •

123\| 123\| •

124\| 124\| if \_\_name\_\_ == \"\_\_main\_\_\":

125\| 125\|     import sys

126\| 126\|     app = QtWidgets.QApplication(sys.argv)

127\| 127\|     RegisterScreen = QtWidgets.QMainWindow()

128\| 128\|     ui = Ui_RegisterScreen()

129\| 129\|     ui.setupUi(RegisterScreen)

130\| 130\|     RegisterScreen.show()

131\| 131\|     sys.exit(app.exec\_())

132\| 132\| •

133\| ​

### Main window

1 \| from PyQt5 import QtCore, QtGui, QtWidgets

2 \| from Player_table import PlayerTable

3 \| from Optimiser import Ui_OptimiserScreen

4 \| ​

5 \| ​

6 \| class Ui_MainScreen(object):

7 \|     

8 \|     def OpenPlayerTable(self):

9 \|         self.window = PlayerTable()

10\|         self.window.show()

11\| ​

12\|     def OpenOptimiser(self):

13\|         self.window = QtWidgets.QMainWindow()

14\|         self.ui = Ui_OptimiserScreen()

15\|         self.ui.setupUi(self.window)

16\|         self.window.show()

17\|               

18\|     def setupUi(self, MainScreen):

19\|         MainScreen.setObjectName(\"MainScreen\")

20\|         MainScreen.resize(800, 600)

21\|         MainScreen.setStyleSheet(\"background-color: rgb(81, 81,
81)\")

22\|         self.centralwidget = QtWidgets.QWidget(MainScreen)

23\|         self.centralwidget.setObjectName(\"centralwidget\")

24\|         self.label = QtWidgets.QLabel(self.centralwidget)

25\|         self.label.setGeometry(QtCore.QRect(60, 70, 661, 71))

26\|         self.label.setStyleSheet(\"font: 24pt \\\"MS Shell Dlg
2\\\";\\n\"

27\| \"color: rgb(255, 255, 255);\")

28\|         self.label.setObjectName(\"label\")

29\|         self.pushButton = QtWidgets.QPushButton(self.centralwidget,
clicked = lambda: self.OpenPlayerTable()) #Button to open the player
table

30\|         self.pushButton.setGeometry(QtCore.QRect(270, 220, 211,
51))

31\|         self.pushButton.setStyleSheet(\"color: rgb(255, 255,
255);\\n\"

32\| \"font: 16pt \\\"MS Shell Dlg 2\\\";\")

33\|         self.pushButton.setObjectName(\"pushButton\")

34\|         self.pushButton_2 =
QtWidgets.QPushButton(self.centralwidget, clicked = lambda:
self.OpenOptimiser()) #Button to open the optimiser screen

35\|         self.pushButton_2.setGeometry(QtCore.QRect(270, 340, 211,
51))

36\|         self.pushButton_2.setStyleSheet(\"color: rgb(255, 255,
255);\\n\"

37\| \"font: 16pt \\\"MS Shell Dlg 2\\\";\")

38\|         self.pushButton_2.setObjectName(\"pushButton_2\")

39\|         MainScreen.setCentralWidget(self.centralwidget)

40\|         self.menubar = QtWidgets.QMenuBar(MainScreen)

41\|         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))

42\|         self.menubar.setObjectName(\"menubar\")

43\|         MainScreen.setMenuBar(self.menubar)

44\|         self.statusbar = QtWidgets.QStatusBar(MainScreen)

45\|         self.statusbar.setObjectName(\"statusbar\")

46\|         MainScreen.setStatusBar(self.statusbar)

47\| ​

48\|         self.retranslateUi(MainScreen)

49\|         QtCore.QMetaObject.connectSlotsByName(MainScreen)

50\| ​

51\|     def retranslateUi(self, MainScreen):

52\|         \_translate = QtCore.QCoreApplication.translate

53\|         MainScreen.setWindowTitle(\_translate(\"MainScreen\",
\"MainWindow\"))

54\|         self.label.setText(\_translate(\"MainScreen\", \"Welcome to
the NBA Draft Optimiser\"))

55\|         self.pushButton.setText(\_translate(\"MainScreen\",
\"Player List\"))

56\|         self.pushButton_2.setText(\_translate(\"MainScreen\",
\"Optimiser\"))

57\| ​

58\| ​

59\| if \_\_name\_\_ == \"\_\_main\_\_\":

60\|     import sys

61\|     app = QtWidgets.QApplication(sys.argv)

62\|     MainScreen = QtWidgets.QMainWindow()

63\|     ui = Ui_MainScreen()

64\|     ui.setupUi(MainScreen)

65\|     MainScreen.show()

66\|     sys.exit(app.exec\_())

### Player Table

1 \| from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,
QTableWidget, QLineEdit, QTableWidgetItem, QPushButton, QApplication,
QHeaderView, QErrorMessage

2 \| from PyQt5.QtCore import Qt

3 \| import csv

4 \| import sys

5 \| import os

6 \| ​

7 \| class PlayerTable(QWidget):

8 \|     def \_\_init\_\_(self):

9 \|         super(PlayerTable, self).\_\_init\_\_()

10\|         self.setWindowTitle(\"Player Table\")

11\|         self.resize(1098, 852)

12\| ​

13\|         layout = QVBoxLayout()  

14\|         self.setLayout(layout)

15\| ​

16\|         # Create a horizontal layout for search bar and button

17\|         search_layout = QHBoxLayout()

18\|         

19\|         self.search_bar = QLineEdit()

20\|         self.search_bar.setPlaceholderText(\"Enter player name,
position, or any text\...\")

21\|         self.search_bar.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\")

22\|         self.search_bar.returnPressed.connect(self.search_table)  #
Search on Enter key

23\|         search_layout.addWidget(self.search_bar)

24\| ​

25\|         self.search_button = QPushButton(\"Search\")

26\|         self.search_button.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\")

27\|         self.search_button.clicked.connect(self.search_table)  #
Connected to search function

28\|         search_layout.addWidget(self.search_button)

29\| ​

30\|         self.clear_button = QPushButton(\"Clear\")

31\|         self.clear_button.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\")

32\|         self.clear_button.clicked.connect(self.clear_search)  #
Clear search

33\|         search_layout.addWidget(self.clear_button)

34\| ​

35\|         layout.addLayout(search_layout)

36\| ​

37\|         self.table_widget = QTableWidget()

38\|         self.table_widget.setStyleSheet(\"font: 10pt \\\"MS Shell
Dlg 2\\\";\")

39\|         layout.addWidget(self.table_widget)

40\| ​

41\|         # Status label to show search results

42\|         self.status_label = QLineEdit()

43\|         self.status_label.setReadOnly(True)

44\|         self.status_label.setStyleSheet(\"font: 10pt \\\"MS Shell
Dlg 2\\\"; background-color: #f0f0f0;\")

45\|         layout.addWidget(self.status_label)

46\| ​

47\|         self.load_data()

48\| ​

49\|     def ExceptionError(self):      

50\|         error_dialog = QErrorMessage()

51\|         error_dialog.showMessage(\'Error loading data.\')

52\|         error_dialog.exec\_()

53\| ​

54\| ​

55\|     def load_data(self):    

56\|         path = os.path.join(os.path.dirname(\_\_file\_\_),
\"nba_player_stats.csv\")# Use relative path

57\|         try:

58\|             with open(path, \'r\', newline=\'\',
encoding=\'utf-8\') as csvfile:

59\|                 read_csv = csv.reader(csvfile)

60\|                 list_values = list(read_csv)

61\| ​

62\|             if not list_values:

63\|                 print(\"CSV file is empty\")

64\|                 return

65\| ​

66\|             self.table_widget.setRowCount(len(list_values) - 1)

67\|             self.table_widget.setColumnCount(len(list_values\[0\]))

68\|           
 self.table_widget.setHorizontalHeaderLabels(list_values\[0\])

69\| ​

70\|             row = 0

71\|             for value_tuple in list_values\[1:\]:

72\|                 column = 0

73\|                 for value in value_tuple:

74\|                     self.table_widget.setItem(row, column,
QTableWidgetItem(str(value)))

75\|                     column += 1

76\|                 row += 1

77\| ​

78\|             # Auto-resize columns

79\|           
 self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

80\|             

81\|             self.status_label.setText(f\"Loaded
{self.table_widget.rowCount()} players\")

82\|             

83\|         except FileNotFoundError:

84\|             self.status_label.setText(f\"Error: File \'{path}\' not
found\")

85\|         except Exception as e:

86\|             self.ExceptionError()

87\| ​

88\|     def search_table(self):

89\|         search_text = self.search_bar.text().strip().lower()

90\|         

91\|         if not search_text:

92\|             self.status_label.setText(\"Please enter search text\")

93\|             return

94\|         

95\|         matches_found = 0

96\|         

97\|         # Search through all rows

98\|         for row in range(self.table_widget.rowCount()):

99\|             row_matches = False

100\|             

101\|             # Check all columns in the row

102\|             for column in range(self.table_widget.columnCount()):

103\|                 item = self.table_widget.item(row, column)

104\|                 if item and search_text in item.text().lower():

105\|                     row_matches = True

106\|                     break

107\|             

108\|             # Show rows that match, hide rows that don\'t

109\|             if row_matches:

110\|                 self.table_widget.setRowHidden(row, False)

111\|                 matches_found += 1

112\|             else:

113\|                 self.table_widget.setRowHidden(row, True)

114\|         

115\|         # Update status

116\|         if matches_found == 0:

117\|             self.status_label.setText(f\"No results found for
\'{self.search_bar.text()}\'\")

118\|         else:

119\|             self.status_label.setText(f\"Found {matches_found}
player(s) matching \'{self.search_bar.text()}\'\")

120\| ​

121\|     def clear_search(self):

122\|         self.search_bar.clear()

123\|         

124\|         # Show all rows

125\|         for row in range(self.table_widget.rowCount()):

126\|             self.table_widget.setRowHidden(row, False)

127\|         

128\|         self.status_label.setText(f\"Showing all
{self.table_widget.rowCount()} players\")

129\| ​

130\| ​

131\| if \_\_name\_\_ == \"\_\_main\_\_\":

132\|     app = QApplication(sys.argv)

133\|     main_window = PlayerTable()

134\|     main_window.showMaximized()

135\|     sys.exit(app.exec\_())     

### Optimiser

1 \| from PyQt5 import QtCore, QtGui, QtWidgets

2 \| from functools import total_ordering

3 \| import csv

4 \| import sys

5 \| import os

6 \| import openpyxl

7 \| import pandas as pd

8 \| from nba_api.stats.endpoints import leaguedashplayerstats,
commonplayerinfo

9 \| import time as time_module

10\| from pulp import \*

11\| from OptimisedTable import OptimisedTable

12\| from FilterTable import FilterTable

13\| ​

14\| ​

15\| class Ui_OptimiserScreen(object):

16\|     

17\|     def \_\_init\_\_(self):

18\|         self.included_playerID = \[\] \# List to store player IDs
that must be included in the lineup

19\|         self.excluded_playerID = \[\] \# List to store player IDs
that must be excluded from the lineup

20\|         self.window = None

21\|         self.filter_window = None

22\| ​

23\|     def OpenOptimiserTable(self): \# Opens the optimised lineup
window

24\|         self.window = OptimisedTable()

25\|         self.window.show()

26\| ​

27\|     def OpenFilterTable(self): \# opens table used to filter
players

28\|         self.filter_window = FilterTable()

29\|       
 self.filter_window.filter_button.clicked.connect(self.get_filtered_players)

30\|         self.filter_window.show()

31\|   

32\|     def get_filtered_players(self):

33\|         self.included_playerID, self.excluded_playerID =
self.filter_window.apply_filters() \# Retrieves the included and
excluded player IDs from the filter table when the \"Apply Filters\"
button is clicked

34\|         return self.included_playerID, self.excluded_playerID

35\| ​

36\|     def num_lineup_error(self): \# error dialog if no lineups are
selected

37\|         error_dialog = QtWidgets.QErrorMessage()

38\|         error_dialog.showMessage(\'Please select the number of
lineups to generate\')

39\|         error_dialog.exec\_()

40\| ​

41\|     def postional_value_error(self): \# error dialog if positional
constraints are not valid (not a number or negative)

42\|         error_dialog = QtWidgets.QErrorMessage()

43\|         error_dialog.showMessage(\'Please enter valid positional
constraints\')

44\|         error_dialog.exec\_()

45\| ​

46\|     def empty_lineup_error(self): \# error dialog if positional
constraints are empty

47\|         error_dialog = QtWidgets.QErrorMessage()

48\|         error_dialog.showMessage(\'Positional constraints cannot be
empty\')

49\|         error_dialog.exec\_()

50\| ​

51\|     def collect_nba_player_stats(season=\'2024-25\',
output_file=\'nba_player_stats.csv\'):

52\| ​

53\|         print(f\"Season = {season}, output file = {output_file}\")
\# terminal read during testing

54\|         

55\|         try:

56\|                 # Step 1: Fetch player stats for the specified
season using leaguedashplayerstats

57\|                 stats =
leaguedashplayerstats.LeagueDashPlayerStats(

58\|                         season=season,

59\|                         per_mode_detailed=\'PerGame\', \# Get per
game stats for easier fantasy point calculation

60\|                         season_type_all_star=\'Regular Season\' \#
Only regular season stats, exclude pre-season and playoffs

61\|                )

62\|                 

63\|                 df = stats.get_data_frames()\[0\] \# Get the first
DataFrame which contains player stats

64\| ​

65\|                 

66\|                 # Step 2: Get positions for each player using
commonplayerinfo        

67\|                 position_map = {} \# Dictionary to store player ID
to position mapping

68\|                 total_players = len(df) \# Total number of players
to process

69\|                 

70\|                 # Loop through each player and fetch their position

71\|                 for idx, player_id in
enumerate(df\[\'PLAYER_ID\'\], 1):

72\|                         try:

73\|                                 if idx % 50 == 0:

74\|                                         print(f\"Progress:
{idx}/{total_players}\") #Progress update every 50 players

75\|                                 player_info =
commonplayerinfo.CommonPlayerInfo(player_id=player_id) \# Make API call
to get player info, including position

76\|                                 player_info_df =
player_info.get_data_frames()\[0\] \# Get the first DataFrame which
contains player info

77\|                                 

78\|                                 if not player_info_df.empty and
\'POSITION\' in player_info_df.columns: \# Check if the DataFrame is not
empty and contains the POSITION column

79\|                                         position =
player_info_df\[\'POSITION\'\].iloc\[0\] \# Get the position of the
player

80\|                                         position_map\[player_id\] =
position

81\|                                 else:

82\|                                         position_map\[player_id\] =
\'N/A\' \# If position is not available, set it to \'N/A\'

83\|                                 

84\|                                 # Rate limiting so API calls dont
get blocked

85\|                                 time_module.sleep(0.6)

86\|                                 

87\|                         except Exception as e:

88\|                                 error_dialog =
QtWidgets.QErrorMessage()

89\|                                 error_dialog.showMessage(f\'Error
fetching position for player ID {player_id}: {e}\')

90\|                                 error_dialog.exec\_()

91\|                                 continue

92\|                 

93\|                 print(f\"Successfully fetched positions for
{len(position_map)} players\") \# Debug statement to check how many
positions were fetched

94\|                 

95\|                 # Step 3: Select required columns

96\|                 player_data = df\[\[

97\|                         \'PLAYER_ID\',

98\|                         \'PLAYER_NAME\',

99\|                         \'TEAM_ABBREVIATION\',

100\|                         \'PTS\',

101\|                         \'REB\',

102\|                         \'AST\',

103\|                         \'STL\',

104\|                         \'BLK\',

105\|                         \'TOV\'

106\|                \]\].copy()

107\|                 

108\|                 # Step 4: Add position using the mapping

109\|                 player_data\[\'Position\'\] =
player_data\[\'PLAYER_ID\'\].map(position_map)

110\|                 

111\|                 # Fill missing positions

112\|                 player_data\[\'Position\'\] =
player_data\[\'Position\'\].fillna(\'N/A\')

113\|                 

114\|                 positions_found =
player_data\[\'Position\'\].notna().sum()

115\|                 print(f\"Positions matched for {positions_found}
out of {len(player_data)} players\")

116\|                 

117\|                 # Step 5: Rename columns

118\|                 player_data.columns = \[

119\|                         \'NBA_ID\',

120\|                         \'Full_Name\',

121\|                         \'Team\',

122\|                         \'Points\',

123\|                         \'Rebounds\',

124\|                         \'Assists\',

125\|                         \'Steals\',

126\|                         \'Blocks\',

127\|                         \'Turnovers\',

128\|                         \'Position\'

129\|                \]

130\|                 

131\|                 # Step 6: Reorder columns

132\|                 player_data = player_data\[\[

133\|                         \'NBA_ID\',

134\|                         \'Full_Name\',

135\|                         \'Team\',

136\|                         \'Position\',

137\|                         \'Points\',

138\|                         \'Rebounds\',

139\|                         \'Assists\',

140\|                         \'Steals\',

141\|                         \'Blocks\',

142\|                         \'Turnovers\'

143\|                \]\]

144\|         

145\|                 # This process can be further optimized by
fetching all player info in bulk if the API supports it

146\| ​

147\|                 # Step 7: Calculate fantasy points

148\|                 # FP = POINTS + (1.2 \* REB) + (1.5 \* AST) + (3
\* STL) + (3 \* BLK) -- TOV

149\|                 player_data\[\'Fantasy_Points\'\] = (

150\|                         player_data\[\'Points\'\] +

151\|                        (1.2 \* player_data\[\'Rebounds\'\]) +

152\|                        (1.5 \* player_data\[\'Assists\'\]) +

153\|                        (3 \* player_data\[\'Steals\'\]) +

154\|                        (3 \* player_data\[\'Blocks\'\]) -

155\|                         player_data\[\'Turnovers\'\]

156\|                )

157\|                 

158\|                 # Round fantasy points to 2 decimal places

159\|                 player_data\[\'Fantasy_Points\'\] =
player_data\[\'Fantasy_Points\'\].round(2)

160\|                 

161\|                 # Step 8: Sort by fantasy points

162\|                 player_data =
player_data.sort_values(\'Fantasy_Points\', ascending=False)

163\|                 

164\|                 # Reset index

165\|                 player_data = player_data.reset_index(drop=True)

166\|                 

167\|                 # Step 9: Save to CSV

168\|                 player_data.to_csv(output_file, index=False)

169\| ​

170\|                 success_dialog = QtWidgets.QErrorMessage()

171\|                 success_dialog.showMessage(\'Player list updated
successfully.\')

172\|                 success_dialog.exec\_()

173\|                 

174\|                 return player_data

175\|                 

176\|         except Exception as e:

177\|                 error_dialog = QtWidgets.QErrorMessage()

178\|                 error_dialog.showMessage(f\'Error updating player
list: {e}\')

179\|                 error_dialog.exec\_()

180\| ​

181\|                 import traceback

182\|                 traceback.print_exc()

183\|                 return None

184\| ​

185\|     def run_optimiser(self):

186\|         # Select no of lineups

187\|         if self.FiveLineups.isChecked():

188\|                 num_lineups = 5

189\|         elif self.TenLineups.isChecked():

190\|                 num_lineups = 10

191\|         elif self.TwentyLineups.isChecked():

192\|                 num_lineups = 20

193\|         else:

194\|                 self.num_lineup_error()

195\|                 return

196\|         

197\|         if not (self.PGValue.text().isdigit() and
self.SFValue.text().isdigit() and self.CValue.text().isdigit()): \#
Check if the positional constraints are valid integers

198\|                 self.postional_value_error()

199\|                 return

200\|         

201\|         if int(self.PGValue.text()) \< 0 or
int(self.SFValue.text()) \< 0 or int(self.CValue.text()) \< 0 or
(int(self.PGValue.text())+int(self.SFValue.text())+int(self.CValue.text()))
\> 20: \# Check if the positional constraints are non-negative and
within bounds

202\|                 self.postional_value_error()

203\|                 return

204\|         if self.PGValue.text() == \"\" or self.SFValue.text() ==
\"\" or self.CValue.text() == \"\": \# Check if the positional
constraints are not empty

205\|                 self.empty_lineup_error()

206\|                 return

207\|         

208\|         num_g = int(self.PGValue.text()) \# Number of guards

209\|         num_f = int(self.SFValue.text()) \# Number of forwards

210\|         num_c = int(self.CValue.text()) \# Number of centers

211\| ​

212\|         # Load player data

213\|         players =
pd.read_csv(os.path.join(os.path.dirname(\_\_file\_\_),
\"nba_player_stats.csv\"))

214\|         

215\|         # Function to expand multi-positional players

216\|         def expand_positions(df):

217\|                 expanded_rows = \[\]

218\|                 for index, row in df.iterrows():

219\|                         positions =
row\[\'Position\'\].split(\'-\')  # Split multi-positions like \"G-F\"
into \[\"G\", \"F\"\]

220\|                         for pos in positions:

221\|                                 secondary_position = row.copy() \#
Create a copy of the original row for each position

222\|                                 secondary_position\[\'Position\'\]
= pos.strip() \# Update position to the current one in the loop

223\|                               
 expanded_rows.append(secondary_position)

224\|                 return pd.DataFrame(expanded_rows)

225\|         

226\|         # Expand players with multiple positions

227\|         players_expanded = expand_positions(players)

228\|         

229\|         # Create workbook for output

230\|         wb = openpyxl.Workbook()

231\|         ws = wb.active

232\|         

233\|         headers = \[\]

234\|         for pos, count in \[(\"Guard\", num_g), (\"Forward\",
num_f), (\"Center\", num_c)\]: \# Create headers like \"Guard 1\",
\"Guard 2\", etc. based on the number of players required for each
position

235\|                 for i in range(1, count + 1): \# Loop to create
headers for each position based on the number of players required

236\|                         headers.append(f\"{pos} {i}\")

237\|         headers.append(\"Total Fantasy Points\")

238\| ​

239\|         for col, header in enumerate(headers, 1):

240\|                 ws.cell(row=1, column=col).value = header \# Write
headers to the first row of the Excel sheet

241\|                 ws.cell(row=1, column=col).font =
openpyxl.styles.Font(bold=True)

242\|         

243\|         # Group players by position and NBA_ID to avoid duplicates

244\|         availables = players_expanded\[\[\'Position\', \'NBA_ID\',
\'Fantasy_Points\', \'Full_Name\'\]\].copy() \# Create a new DataFrame
with only the necessary columns for optimization

245\|         

246\|         # Create points dictionary for each position

247\|         points = {}

248\|         for pos in availables.Position.unique():

249\|                 availables_pos = availables\[availables.Position
== pos\] \# Filter players for the current position

250\|                 pos_points = list(availables_pos\[\[\'NBA_ID\',
\'Fantasy_Points\'\]\].set_index(\'NBA_ID\').to_dict().values())\[0\] \#
Create a dictionary of player ID to fantasy points for the current
position

251\|                 points\[pos\] = pos_points

252\|         

253\|         # Dictionary to store the number of players required for
each position based on user input

254\|         pos_num_available = {

255\|                 \"Guard\": num_g,  

256\|                 \"Forward\": num_f,  

257\|                 \"Center\": num_c  

258\|        }

259\|         

260\|         # Generate multiple lineups

261\|         previous_lineups = \[\]

262\|         

263\|         for lineup_num in range(1, num_lineups + 1):

264\|                 # Create binary variables for each player in each
position

265\|                 \_vars = {k: LpVariable.dicts(k, v.keys(),
cat=\'Binary\') for k, v in points.items()} \# Create a dictionary of
binary variables for each position and player ID, where the variable is
1 if the player is selected for that position and 0 otherwise

266\|                 

267\|                 prob = LpProblem(\"Fantasy Lineups\", LpMaximize)
\# Create a linear programming problem to maximize fantasy points

268\| ​

269\| ​

270\|                 # Objective: maximize total points

271\|                 total_points = \[\]

272\|                 for pos, players_dict in points.items(): \# Loop
through each position and its corresponding player dictionary to
calculate the total fantasy points for the lineup based on the selected
players

273\|                         for player_id, player_points in
players_dict.items():

274\|                                 total_points.append(player_points
\* \_vars\[pos\]\[player_id\]) \# Multiply the fantasy points of each
player by the corresponding binary variable to include it in the total
points calculation only if the player is selected for the lineup

275\|                 

276\|                 prob += lpSum(total_points)

277\|                 

278\|                 # Position constraints

279\|                 for pos in points.keys():

280\|                         prob += lpSum(\[\_vars\[pos\]\[player_id\]
for player_id in points\[pos\]\]) == pos_num_available\[pos\] \# Ensure
that the number of players selected for each position matches the
user-defined constraints (e.g., exactly 2 guards, 2 forwards, 1 center)

281\|                 

282\|                 # CRITICAL: Each player can only be selected once
across all positions

283\|                 all_player_ids = set()

284\|                 for pos in points.keys():

285\|                       
 all_player_ids.update(points\[pos\].keys())

286\|                 

287\|                 for player_id in all_player_ids:

288\|                         player_vars = \[\]

289\|                         for pos in points.keys():

290\|                                 if player_id in points\[pos\]:

291\|                                       
 player_vars.append(\_vars\[pos\]\[player_id\])

292\|                         if player_vars:

293\|                                 prob += lpSum(player_vars) \<= 1
 # Each player used at most once

294\| ​

295\|                 # Include/exclude player constraints

296\|                 for included_player_id in self.included_playerID:

297\|                         player_positions = \[\]

298\|                         for pos in points.keys():

299\|                                 if included_player_id in
points\[pos\]:

300\|                                       
 player_positions.append(\_vars\[pos\]\[included_player_id\])

301\|             

302\|                         if player_positions:

303\|                                 prob += lpSum(player_positions) ==
1  # Must be selected at exactly one position

304\| ​

305\|                 # Exclude player constraints

306\|                 for excluded_player_id in self.excluded_playerID:

307\|                         for pos in points.keys():

308\|                                 if excluded_player_id in
points\[pos\]:

309\|                                         prob +=
\_vars\[pos\]\[excluded_player_id\] == 0

310\|                 

311\|                 # Exclude previous lineups

312\|                 for prev_lineup in previous_lineups:

313\|                         prob += lpSum(\[\_vars\[pos\]\[player_id\]
for pos, player_id in prev_lineup\]) \<= len(prev_lineup) - 1

314\|                 

315\|                 # Solve

316\|                 prob.solve()

317\|                 

318\|                 if prob.status != 1:

319\|                         print(f\"No optimal solution found for
lineup {lineup_num}\")

320\|                         break

321\|                 

322\|                 # Extract selected players

323\|                 selected_players = \[\]

324\|                 total_score = 0

325\|                 lineup_players = {\'Guard\': \[\], \'Forward\':
\[\], \'Center\': \[\]}

326\|                 

327\|                 for pos in points.keys():

328\|                         for player_id in points\[pos\]:

329\|                                 if
\_vars\[pos\]\[player_id\].varValue == 1:

330\|                                         player_name =
availables\[(availables.NBA_ID == player_id) &

331\|                                               
(availables.Position == pos)\]\[\'Full_Name\'\].values\[0\]

332\|                                         player_points =
points\[pos\]\[player_id\]

333\|                         

334\|                                       
 lineup_players\[pos\].append(f\"{player_name} ({player_points:.1f})\")

335\|                                       
 selected_players.append((pos, player_id))

336\|                                         total_score +=
player_points

337\|                 

338\|                 # Write to Excel

339\|                 row = lineup_num + 1

340\|                 col = 1

341\|                 

342\|                 for pos in \[\'Guard\', \'Forward\', \'Center\'\]:

343\|                         players_in_pos = lineup_players\[pos\]

344\|                         for i in range(pos_num_available\[pos\]):

345\|                                 if i \< len(players_in_pos):

346\|                                         ws.cell(row=row,
column=col).value = players_in_pos\[i\]

347\|                                 col += 1

348\|                 

349\|                 ws.cell(row=row, column=col).value =
round(total_score, 2)

350\|                 

351\|                 previous_lineups.append(selected_players)

352\|                 

353\| ​

354\|                 print(f\"Lineup {lineup_num}: Total Fantasy Points
= {total_score:.2f}\")

355\|                 print(f\"Guards: {lineup_players\[\'Guard\'\]}\")

356\|                 print(f\"Forwards:
{lineup_players\[\'Forward\'\]}\")

357\|                 print(f\"Centers:
{lineup_players\[\'Center\'\]}\")

358\|         

359\|         wb.save(\"fantasy_lineups.xlsx\")

360\|         self.OpenOptimiserTable()

361\|     

362\|     def setupUi(self, OptimiserScreen):

363\|         OptimiserScreen.setObjectName(\"OptimiserScreen\")

364\|         OptimiserScreen.resize(1098, 852)

365\|         OptimiserScreen.setStyleSheet(\"background-color: rgb(81,
81, 81);\")

366\|         self.centralwidget = QtWidgets.QWidget(OptimiserScreen)

367\|         self.centralwidget.setObjectName(\"centralwidget\")

368\|         self.Heading = QtWidgets.QLabel(self.centralwidget)

369\|         self.Heading.setGeometry(QtCore.QRect(360, 20, 331, 81))

370\|         self.Heading.setStyleSheet(\"color: rgb(255, 255,
255);\\n\"

371\|         \"text-decoration: underline;\\n\"

372\|         \"font: 8pt \\\"MS Shell Dlg 2\\\";\\n\"

373\|         \"font: 24pt \\\"MS Shell Dlg 2\\\";\")

374\|         self.Heading.setObjectName(\"Heading\")

375\|         self.FiveLineups =
QtWidgets.QRadioButton(self.centralwidget)

376\|         self.FiveLineups.setGeometry(QtCore.QRect(250, 250, 121,
21))

377\|         self.FiveLineups.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\\n\"

378\| \"color: rgb(255, 255, 255);\")

379\|         self.FiveLineups.setObjectName(\"FiveLineups\")

380\|         

381\|         self.LineupNumberLabel =
QtWidgets.QLabel(self.centralwidget)

382\|         self.LineupNumberLabel.setGeometry(QtCore.QRect(30, 240,
171, 41))

383\|         self.LineupNumberLabel.setStyleSheet(\"font: 12pt \\\"MS
Shell Dlg 2\\\";\\n\"

384\| \"color: rgb(255, 255, 255);\")

385\|       
 self.LineupNumberLabel.setObjectName(\"LineupNumberLabel\")

386\| ​

387\|         self.PGValue = QtWidgets.QLineEdit(self.centralwidget)

388\|         self.PGValue.setGeometry(QtCore.QRect(150, 420, 41, 22))

389\|         self.PGValue.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\\n\"

390\| \"color: rgb(255, 255, 255);\")

391\|         self.PGValue.setPlaceholderText(\"2\")

392\|         self.PGValue.setObjectName(\"PGValue\")

393\| ​

394\|         self.SFValue = QtWidgets.QLineEdit(self.centralwidget)

395\|         self.SFValue.setGeometry(QtCore.QRect(150, 500, 41, 22))

396\|         self.SFValue.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\\n\"

397\| \"color: rgb(255, 255, 255);\")

398\|         self.SFValue.setPlaceholderText(\"2\")

399\|         self.SFValue.setObjectName(\"SFValue\")

400\| ​

401\|         self.CValue = QtWidgets.QLineEdit(self.centralwidget)

402\|         self.CValue.setPlaceholderText(\"1\")

403\|         self.CValue.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\\n\"

404\| \"color: rgb(255, 255, 255);\")

405\|         self.CValue.setGeometry(QtCore.QRect(150, 580, 41, 22))

406\|         self.CValue.setObjectName(\"CValue\")

407\| ​

408\|         self.PGLabel = QtWidgets.QLabel(self.centralwidget)

409\|         self.PGLabel.setGeometry(QtCore.QRect(40, 420, 100, 16))

410\|         self.PGLabel.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\\n\"

411\| \"color: rgb(255, 255, 255);\")

412\|         self.PGLabel.setObjectName(\"PGLabel\")

413\| ​

414\|         self.TenLineups =
QtWidgets.QRadioButton(self.centralwidget)

415\|         self.TenLineups.setGeometry(QtCore.QRect(460, 250, 121,
21))

416\|         self.TenLineups.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\\n\"

417\| \"color: rgb(255, 255, 255);\")

418\|         self.TenLineups.setObjectName(\"TenLineups\")

419\| ​

420\|         self.TwentyLineups =
QtWidgets.QRadioButton(self.centralwidget)

421\|         self.TwentyLineups.setGeometry(QtCore.QRect(720, 250, 121,
21))

422\|         self.TwentyLineups.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\\n\"

423\| \"color: rgb(255, 255, 255);\")

424\|         self.TwentyLineups.setObjectName(\"TwentyLineups\")

425\| ​

426\|         self.SFLabel = QtWidgets.QLabel(self.centralwidget)

427\|         self.SFLabel.setGeometry(QtCore.QRect(40, 500, 100, 16))

428\|         self.SFLabel.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\\n\"

429\| \"color: rgb(255, 255, 255);\")

430\|         self.SFLabel.setObjectName(\"SFLabel\")

431\| ​

432\|         self.CLabel = QtWidgets.QLabel(self.centralwidget)

433\|         self.CLabel.setGeometry(QtCore.QRect(40, 580, 100, 16))

434\|         self.CLabel.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\\n\"

435\| \"color: rgb(255, 255, 255);\")

436\|         self.CLabel.setObjectName(\"CLabel\")

437\| ​

438\|         self.CreateLineupButton =
QtWidgets.QPushButton(self.centralwidget, clicked = lambda:
self.run_optimiser())

439\|         self.CreateLineupButton.setGeometry(QtCore.QRect(420, 680,
241, 61))

440\|         self.CreateLineupButton.setStyleSheet(\"font: 16pt \\\"MS
Shell Dlg 2\\\";\\n\"

441\| \"color: rgb(255, 255, 255);\")

442\|       
 self.CreateLineupButton.setObjectName(\"CreateLineupButton\")

443\| ​

444\|         self.FilterPlayersButton =
QtWidgets.QPushButton(self.centralwidget, clicked = lambda:
self.OpenFilterTable())

445\|         self.FilterPlayersButton.setGeometry(QtCore.QRect(650,
430, 121, 41))

446\|         self.FilterPlayersButton.setStyleSheet(\"color: rgb(255,
255, 255);\\n\"

447\| \"font: 12pt \\\"MS Shell Dlg 2\\\";\")

448\|         

449\|       
 self.FilterPlayersButton.setObjectName(\"FilterPlayersButton\")

450\|         self.PositionalConstraintLabel =
QtWidgets.QLabel(self.centralwidget)

451\|       
 self.PositionalConstraintLabel.setGeometry(QtCore.QRect(30, 340, 271,
41))

452\|         self.PositionalConstraintLabel.setStyleSheet(\"font: 16pt
\\\"MS Shell Dlg 2\\\";\\n\"

453\| \"text-decoration: underline;\\n\"

454\| \"color: rgb(255, 255, 255);\")

455\|       
 self.PositionalConstraintLabel.setObjectName(\"PositionalConstraintLabel\")

456\| ​

457\|         self.PlayerConstraintLabel =
QtWidgets.QLabel(self.centralwidget)

458\|         self.PlayerConstraintLabel.setGeometry(QtCore.QRect(630,
340, 271, 41))

459\|         self.PlayerConstraintLabel.setStyleSheet(\"font: 16pt
\\\"MS Shell Dlg 2\\\";\\n\"

460\| \"text-decoration: underline;\\n\"

461\| \"color: rgb(255, 255, 255);\")

462\|       
 self.PlayerConstraintLabel.setObjectName(\"PlayerConstraintLabel\")

463\| ​

464\|         self.UpdatePlayerLabel =
QtWidgets.QLabel(self.centralwidget)

465\|         self.UpdatePlayerLabel.setGeometry(QtCore.QRect(30, 140,
171, 31))

466\|         self.UpdatePlayerLabel.setStyleSheet(\"font: 12pt \\\"MS
Shell Dlg 2\\\";\\n\"

467\| \"color: rgb(255, 255, 255);\")

468\|       
 self.UpdatePlayerLabel.setObjectName(\"UpdatePlayerLabel\")

469\| ​

470\|         self.UpdateButton =
QtWidgets.QPushButton(self.centralwidget, clicked = lambda:
self.collect_nba_player_stats())

471\|         self.UpdateButton.setGeometry(QtCore.QRect(230, 140, 111,
31))

472\|         self.UpdateButton.setStyleSheet(\"color: rgb(255, 255,
255);\")

473\|         self.UpdateButton.setObjectName(\"UpdateButton\")

474\| ​

475\|         OptimiserScreen.setCentralWidget(self.centralwidget)

476\|         self.menubar = QtWidgets.QMenuBar(OptimiserScreen)

477\|         self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))

478\|         self.menubar.setObjectName(\"menubar\")

479\|         OptimiserScreen.setMenuBar(self.menubar)

480\|         self.statusbar = QtWidgets.QStatusBar(OptimiserScreen)

481\|         self.statusbar.setObjectName(\"statusbar\")

482\|         OptimiserScreen.setStatusBar(self.statusbar)

483\| ​

484\|         self.retranslateUi(OptimiserScreen)

485\|         QtCore.QMetaObject.connectSlotsByName(OptimiserScreen)

486\| ​

487\|     def retranslateUi(self, OptimiserScreen):                    
                                     

488\|         \_translate = QtCore.QCoreApplication.translate

489\|       
 OptimiserScreen.setWindowTitle(\_translate(\"OptimiserScreen\",
\"MainWindow\"))

490\|         self.Heading.setText(\_translate(\"OptimiserScreen\",
\"Optimiser Settings\"))

491\|         self.FiveLineups.setText(\_translate(\"OptimiserScreen\",
\"5\"))

492\|       
 self.LineupNumberLabel.setText(\_translate(\"OptimiserScreen\",
\"Number of lineups\"))

493\|         self.PGLabel.setText(\_translate(\"OptimiserScreen\",
\"Guard\"))

494\|         self.TenLineups.setText(\_translate(\"OptimiserScreen\",
\"10\"))

495\|       
 self.TwentyLineups.setText(\_translate(\"OptimiserScreen\", \"20\"))

496\|         self.SFLabel.setText(\_translate(\"OptimiserScreen\",
\"Forward\"))

497\|         self.CLabel.setText(\_translate(\"OptimiserScreen\",
\"Center\"))

498\|       
 self.CreateLineupButton.setText(\_translate(\"OptimiserScreen\",
\"Create lineup\"))

499\|       
 self.PositionalConstraintLabel.setText(\_translate(\"OptimiserScreen\",
\"Positional Constraints\"))

500\|       
 self.PlayerConstraintLabel.setText(\_translate(\"OptimiserScreen\",
\"Player Constraints\"))

501\|       
 self.UpdatePlayerLabel.setText(\_translate(\"OptimiserScreen\",
\"Update player list\"))

502\|         self.UpdateButton.setText(\_translate(\"OptimiserScreen\",
\"Update\"))

503\|       
 self.FilterPlayersButton.setText(\_translate(\"OptimiserScreen\",
\"Filter Players\"))

504\| ​

505\| if \_\_name\_\_ == \"\_\_main\_\_\":

506\|     app = QtWidgets.QApplication(sys.argv)

507\|     OptimiserScreen = QtWidgets.QMainWindow()

508\|     ui = Ui_OptimiserScreen()

509\|     ui.setupUi(OptimiserScreen)

510\|     OptimiserScreen.show()

511\|     sys.exit(app.exec\_())

### Optimised Table

1 \| from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,
QTableWidget, QLineEdit, QTableWidgetItem, QPushButton, QApplication,
QHeaderView, QCheckBox, QFileDialog, QErrorMessage

2 \| from PyQt5.QtCore import Qt

3 \| import openpyxl

4 \| import os

5 \| import csv

6 \| import sys

7 \| import json

8 \| ​

9 \| class OptimisedTable(QWidget):

10\|     def \_\_init\_\_(self):

11\|         super(OptimisedTable, self).\_\_init\_\_()

12\|         self.setWindowTitle(\"Optimised Table\")

13\|         self.resize(1098, 852)

14\| ​

15\|         layout = QVBoxLayout()  

16\|         self.setLayout(layout)

17\| ​

18\|         # Create a horizontal layout for search bar and button

19\|         search_layout = QHBoxLayout()

20\|         

21\|         self.search_bar = QLineEdit()

22\|         self.search_bar.setPlaceholderText(\"Enter player name,
position, or any text\...\")

23\|         self.search_bar.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\")

24\|         self.search_bar.returnPressed.connect(self.search_table)  #
Search on Enter key

25\|         search_layout.addWidget(self.search_bar)

26\| ​

27\|         self.search_button = QPushButton(\"Search\")

28\|         self.search_button.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\")

29\|         self.search_button.clicked.connect(self.search_table)  #
Connected to search function

30\|         search_layout.addWidget(self.search_button)

31\| ​

32\|         self.clear_button = QPushButton(\"Clear\")

33\|         self.clear_button.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\")

34\|         self.clear_button.clicked.connect(self.clear_search)  #
Clear search

35\|         search_layout.addWidget(self.clear_button)

36\| ​

37\|         self.save_csv_button = QPushButton(\"Save as CSV\")

38\|         self.save_csv_button.setStyleSheet(\"font: 12pt \\\"MS
Shell Dlg 2\\\";\")

39\|         search_layout.addWidget(self.save_csv_button)

40\|         self.save_csv_button.clicked.connect(self.save_csv)  # Save
selected players

41\| ​

42\|         self.save_json_button = QPushButton(\"Save as JSON\")

43\|         self.save_json_button.clicked.connect(self.save_json)  #
Save selected players

44\|         self.save_json_button.setStyleSheet(\"font: 12pt \\\"MS
Shell Dlg 2\\\";\")

45\|         search_layout.addWidget(self.save_json_button)

46\| ​

47\|         layout.addLayout(search_layout)

48\| ​

49\|         self.table_widget = QTableWidget()

50\|         self.table_widget.setStyleSheet(\"font: 10pt \\\"MS Shell
Dlg 2\\\";\")

51\|         layout.addWidget(self.table_widget)

52\| ​

53\|         # Status label to show search results

54\|         self.status_label = QLineEdit()

55\|         self.status_label.setReadOnly(True)

56\|         self.status_label.setStyleSheet(\"font: 10pt \\\"MS Shell
Dlg 2\\\"; background-color: #f0f0f0;\")

57\|         layout.addWidget(self.status_label)

58\| ​

59\|         self.load_data()

60\| ​

61\|     def ExceptionError(self):      

62\|         error_dialog = QErrorMessage()

63\|         error_dialog.showMessage(\'Error loading data.\')

64\|         error_dialog.exec\_()

65\| ​

66\|     def load_data(self):    

67\|         path = os.path.join(os.path.dirname(\_\_file\_\_),
\"fantasy_lineups.xlsx\")# Use relative path

68\|         try:

69\|             workbook = openpyxl.load_workbook(path)

70\|             sheet = workbook.active

71\| ​

72\|             list_values = list(sheet.values)

73\| ​

74\| ​

75\|             if not list_values:

76\|                 print(\"Excel file is empty\")

77\|                 return

78\| ​

79\|             self.table_widget.setRowCount(len(list_values) - 1)

80\|           
 self.table_widget.setColumnCount(len(list_values\[0\]) + 1)  # Extra
column for Save checkbox

81\|             headers = list(list_values\[0\]) + \[\"Save\"\]

82\|             self.table_widget.setHorizontalHeaderLabels(headers)

83\| ​

84\|             row = 0

85\|             for value_tuple in list_values\[1:\]:

86\|                 column = 0

87\|                 for value in value_tuple:

88\|                     self.table_widget.setItem(row, column,
QTableWidgetItem(str(value)))

89\|                     column += 1

90\| ​

91\|                 SaveCheckbox = QCheckBox()

92\|                 SaveCheckbox.setStyleSheet(\"margin-left:50%;
margin-right:50%;\")

93\|                 self.table_widget.setCellWidget(row, column,
SaveCheckbox)

94\|                 column += 1

95\|                 row += 1

96\| ​

97\|             # Auto-resize columns

98\|           
 self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

99\|             

100\|             self.status_label.setText(f\"Loaded
{self.table_widget.rowCount()} players\")

101\|             

102\|         except FileNotFoundError:

103\|             self.status_label.setText(f\"Error: File \'{path}\'
not found\")

104\|         except Exception as e:

105\|             self.status_label.setText(f\"Error loading data:
{e}\")

106\| ​

107\|     def save_csv(self):

108\|         output_file, \_ = QFileDialog.getSaveFileName(self, \"Save
Selected Players\", \"\", \"CSV Files (\*.csv);;All Files (\*)\")

109\|         if not output_file:

110\|             return  # User cancelled the dialog

111\|         

112\|         try:

113\|             selected_players = \[\]

114\|             headers =
\[self.table_widget.horizontalHeaderItem(col).text() for col in
range(self.table_widget.columnCount() - 1)\]  # Exclude Save column

115\|             selected_players.append(headers)

116\|             

117\|             for row in range(self.table_widget.rowCount()):

118\|                 save_checkbox = self.table_widget.cellWidget(row,
self.table_widget.columnCount() - 1)

119\|                 if save_checkbox.isChecked():

120\|                     player_data = \[\]

121\|                     for col in
range(self.table_widget.columnCount() - 1):  # Exclude Save column

122\|                         item = self.table_widget.item(row, col)

123\|                         player_data.append(item.text() if item
else \"\")

124\|                     selected_players.append(player_data)

125\|             

126\|             if not selected_players or len(selected_players) == 1:

127\|                 error_dialog = QErrorMessage()

128\|                 error_dialog.showMessage(\"No players selected to
save.\")

129\|                 error_dialog.exec\_()

130\|                 return

131\|             

132\|             with open(output_file, \'w\', newline=\'\',
encoding=\'utf-8\') as csvfile:

133\|                 writer = csv.writer(csvfile)

134\|                 writer.writerows(selected_players)

135\|             

136\|             self.status_label.setText(f\"Successfully saved
{len(selected_players) - 1} players to {output_file}\")

137\|         

138\|         except Exception as e:

139\|             self.ExceptionError()

140\| ​

141\|     def save_json(self):

142\|         output_file, \_ = QFileDialog.getSaveFileName(self, \"Save
Selected Players\", \"\", \"JSON Files (\*.json);;All Files (\*)\")

143\|         if not output_file:

144\|             return  # User cancelled the dialog

145\|         

146\|         try:

147\|             selected_players = \[\]

148\|             headers =
\[self.table_widget.horizontalHeaderItem(col).text() for col in
range(self.table_widget.columnCount() - 1)\]  # Exclude Save column

149\|             

150\|             for row in range(self.table_widget.rowCount()):

151\|                 save_checkbox = self.table_widget.cellWidget(row,
self.table_widget.columnCount() - 1)

152\|                 if save_checkbox.isChecked():

153\|                     player_data = {}

154\|                     for col in
range(self.table_widget.columnCount() - 1):  # Exclude Save column

155\|                         item = self.table_widget.item(row, col)

156\|                         player_data\[headers\[col\]\] =
item.text() if item else \"\"

157\|                     selected_players.append(player_data)

158\|             

159\|             if not selected_players:

160\|                 error_dialog = QErrorMessage()

161\|                 error_dialog.showMessage(\"No players selected to
save.\")

162\|                 error_dialog.exec\_()

163\|                 return

164\|             

165\|             with open(output_file, \'w\', encoding=\'utf-8\') as
jsonfile:

166\|                 json.dump(selected_players, jsonfile, indent=4)

167\|             

168\|             self.status_label.setText(f\"Successfully saved
{len(selected_players)} players to {output_file}\")

169\|         

170\|         except Exception as e:

171\|             self.ExceptionError()

172\|             

173\|     def search_table(self):

174\|         search_text = self.search_bar.text().strip().lower()

175\|         

176\|         if not search_text:

177\|             self.status_label.setText(\"Please enter search
text\")

178\|             return

179\|         

180\|         matches_found = 0

181\|         

182\|         # Search through all rows

183\|         for row in range(self.table_widget.rowCount()):

184\|             row_matches = False

185\|             

186\|             # Check all columns in the row

187\|             for column in range(self.table_widget.columnCount()):

188\|                 item = self.table_widget.item(row, column)

189\|                 if item and search_text in item.text().lower():

190\|                     row_matches = True

191\|                     break

192\|             

193\|             # Show rows that match, hide rows that don\'t

194\|             if row_matches:

195\|                 self.table_widget.setRowHidden(row, False)

196\|                 matches_found += 1

197\|             else:

198\|                 self.table_widget.setRowHidden(row, True)

199\|         

200\|         # Update status

201\|         if matches_found == 0:

202\|             self.status_label.setText(f\"No results found for
\'{self.search_bar.text()}\'\")

203\|         else:

204\|             self.status_label.setText(f\"Found {matches_found}
player(s) matching \'{self.search_bar.text()}\'\")

205\| ​

206\|     def clear_search(self):

207\| ​

208\|         self.search_bar.clear()

209\|         

210\|         # Show all rows

211\|         for row in range(self.table_widget.rowCount()):

212\|             self.table_widget.setRowHidden(row, False)

213\|         

214\|         self.status_label.setText(f\"Showing all
{self.table_widget.rowCount()} players\")

215\| ​

216\| ​

217\| if \_\_name\_\_ == \"\_\_main\_\_\":

218\|     app = QApplication(sys.argv)

219\|     main_window = OptimisedTable()

220\|     main_window.showMaximized()

221\|     sys.exit(app.exec\_())

### Filter Table

1 \| from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout,
QTableWidget, QLineEdit, QTableWidgetItem, QPushButton, QApplication,
QHeaderView, QCheckBox

2 \| from PyQt5.QtCore import Qt

3 \| import csv

4 \| import sys

5 \| import os

6 \| ​

7 \| class FilterTable(QWidget):

8 \| ​

9 \| ​

10\|     def \_\_init\_\_(self):

11\|         super(FilterTable, self).\_\_init\_\_()

12\|         self.setWindowTitle(\"Filter Table\")

13\|         self.resize(1098, 852)

14\| ​

15\|         layout = QVBoxLayout()  

16\|         self.setLayout(layout)

17\| ​

18\|         # Create a horizontal layout for search bar and button

19\|         search_layout = QHBoxLayout()

20\|         

21\|         self.search_bar = QLineEdit()

22\|         self.search_bar.setPlaceholderText(\"Enter player name,
position, or any text\...\")

23\|         self.search_bar.setStyleSheet(\"font: 12pt \\\"MS Shell Dlg
2\\\";\")

24\|         self.search_bar.returnPressed.connect(self.search_table)  #
Search on Enter key

25\|         search_layout.addWidget(self.search_bar)

26\| ​

27\|         self.search_button = QPushButton(\"Search\")

28\|         self.search_button.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\")

29\|         self.search_button.clicked.connect(self.search_table)  #
Connected to search function

30\|         search_layout.addWidget(self.search_button)

31\| ​

32\|         self.clear_button = QPushButton(\"Clear\")

33\|         self.clear_button.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\")

34\|         self.clear_button.clicked.connect(self.clear_search)  #
Clear search

35\|         search_layout.addWidget(self.clear_button)

36\| ​

37\|         self.filter_button = QPushButton(\"Apply Filters\")

38\|         self.filter_button.setStyleSheet(\"font: 12pt \\\"MS Shell
Dlg 2\\\";\")

39\|         self.filter_button.clicked.connect(self.apply_filters)  #
Apply filters

40\|         search_layout.addWidget(self.filter_button)

41\| ​

42\|         layout.addLayout(search_layout)

43\| ​

44\|         self.table_widget = QTableWidget()

45\|         self.table_widget.setStyleSheet(\"font: 10pt \\\"MS Shell
Dlg 2\\\";\")

46\|         layout.addWidget(self.table_widget)

47\| ​

48\|         # Status label to show search results

49\|         self.status_label = QLineEdit()

50\|         self.status_label.setReadOnly(True)

51\|         self.status_label.setStyleSheet(\"font: 10pt \\\"MS Shell
Dlg 2\\\"; background-color: #f0f0f0;\")

52\|         layout.addWidget(self.status_label)

53\| ​

54\|         self.load_data()

55\| ​

56\|     def apply_filters(self):

57\|         included_players = \[\]

58\|         excluded_players = \[\]

59\|                 

60\|         for row in range(self.table_widget.rowCount()):

61\|             include_checkbox = self.table_widget.cellWidget(row,
self.table_widget.columnCount() - 2)

62\|             exclude_checkbox = self.table_widget.cellWidget(row,
self.table_widget.columnCount() - 1)

63\|             player_name_item = self.table_widget.item(row, 0)
 #returns NBA_ID of player to make it easier to filter later on

64\|             

65\|             if player_name_item:

66\|                 player_name = player_name_item.text()

67\|                 

68\|                 if include_checkbox and
include_checkbox.isChecked():

69\|                     included_players.append(int(player_name))

70\|                 if exclude_checkbox and
exclude_checkbox.isChecked():

71\|                     excluded_players.append(int(player_name))

72\|         print(f\"Included Players: {included_players}\")

73\|         print(f\"Excluded Players: {excluded_players}\")

74\|         return included_players, excluded_players

75\| ​

76\|     def load_data(self):    

77\|         path = os.path.join(os.path.dirname(\_\_file\_\_),
\"nba_player_stats.csv\")# Use relative path

78\|         try:

79\|             with open(path, \'r\', newline=\'\',
encoding=\'utf-8\') as csvfile:

80\|                 read_csv = csv.reader(csvfile)

81\|                 list_values = list(read_csv)

82\| ​

83\|             if not list_values:

84\|                 print(\"CSV file is empty\")

85\|                 return

86\| ​

87\|             self.table_widget.setRowCount(len(list_values) - 1)

88\|             # Add 2 extra columns for checkboxes

89\|           
 self.table_widget.setColumnCount(len(list_values\[0\]) + 2)

90\|             

91\|             # Set headers with checkbox columns

92\|             headers = list_values\[0\] + \[\"Include\",
\"Exclude\"\]

93\|             self.table_widget.setHorizontalHeaderLabels(headers)

94\| ​

95\|             row = 0

96\|             for value_tuple in list_values\[1:\]:

97\|                 column = 0

98\|                 # Add data columns

99\|                 for value in value_tuple:

100\|                     self.table_widget.setItem(row, column,
QTableWidgetItem(str(value)))

101\|                     column += 1

102\|                 

103\|                 # Add two checkboxes in the last two columns

104\|                 # First checkbox

105\|                 IncludeCheckbox = QCheckBox()

106\|                 IncludeCheckbox.setStyleSheet(\"margin-left:50%;
margin-right:50%;\")

107\|                 self.table_widget.setCellWidget(row, column,
IncludeCheckbox)

108\|                 column += 1

109\|                 

110\|                 # Second checkbox

111\|                 ExcludeCheckbox = QCheckBox()

112\|                 ExcludeCheckbox.setStyleSheet(\"margin-left:50%;
margin-right:50%;\")

113\|                 self.table_widget.setCellWidget(row, column,
ExcludeCheckbox)

114\|                 

115\|                 row += 1

116\| ​

117\|             # Auto-resize columns

118\|           
 self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

119\|             

120\|             self.status_label.setText(f\"Loaded
{self.table_widget.rowCount()} players\")

121\|             

122\|         except FileNotFoundError:

123\|             self.status_label.setText(f\"Error: File \'{path}\'
not found\")

124\|         except Exception as e:

125\|             self.status_label.setText(f\"Error loading data:
{e}\")

126\| ​

127\|     def search_table(self):

128\| ​

129\|         search_text = self.search_bar.text().strip().lower()

130\|         

131\|         if not search_text:

132\|             self.status_label.setText(\"Please enter search
text\")

133\|             return

134\|         

135\|         matches_found = 0

136\|         

137\|         # Search through all rows

138\|         for row in range(self.table_widget.rowCount()):

139\|             row_matches = False

140\|             

141\|             # Check all columns in the row (excluding checkbox
columns)

142\|             for column in range(self.table_widget.columnCount() -
2):

143\|                 item = self.table_widget.item(row, column)

144\|                 if item and search_text in item.text().lower():

145\|                     row_matches = True

146\|                     break

147\|             

148\|             # Show rows that match, hide rows that don\'t

149\|             if row_matches:

150\|                 self.table_widget.setRowHidden(row, False)

151\|                 matches_found += 1

152\|             else:

153\|                 self.table_widget.setRowHidden(row, True)

154\|         

155\|         # Update status

156\|         if matches_found == 0:

157\|             self.status_label.setText(f\"No results found for
\'{self.search_bar.text()}\'\")

158\|         else:

159\|             self.status_label.setText(f\"Found {matches_found}
player(s) matching \'{self.search_bar.text()}\'\")

160\| ​

161\|     def clear_search(self):

162\| ​

163\|         self.search_bar.clear()

164\|         

165\|         # Show all rows

166\|         for row in range(self.table_widget.rowCount()):

167\|             self.table_widget.setRowHidden(row, False)

168\|         

169\|         self.status_label.setText(f\"Showing all
{self.table_widget.rowCount()} players\")

170\| ​

171\| ​

172\| if \_\_name\_\_ == \"\_\_main\_\_\":

173\|     app = QApplication(sys.argv)

174\|     main_window = FilterTable()

175\|     main_window.showMaximized()

176\|     sys.exit(app.exec\_())

## Code Screenshots

### Login

![](media/image39.png){width="6.0625in" height="6.604166666666667in"}

### Register

![](media/image40.png){width="6.09375in" height="6.645833333333333in"}

### Main Window

![](media/image41.png){width="6.268055555555556in"
height="4.917361111111111in"}

### Player Table

![](media/image42.png){width="6.268055555555556in"
height="5.013194444444444in"}

### Optimiser

![](media/image43.png){width="6.268055555555556in" height="5.0125in"}

### Filter Table

![](media/image44.png){width="6.268055555555556in"
height="5.029166666666667in"}

### Optimised Table

![](media/image45.png){width="6.268055555555556in"
height="5.039583333333334in"}

## Bibliography

AUTHORS, See. "Openpyxl: A Python Library to Read/Write Excel 2010
Xlsx/Xlsm Files." *PyPI*, pypi.org/project/openpyxl/.

"Fantasy Basketball - Leagues, Rankings, News, Picks & More."
*ESPN.com*, www.espn.com/fantasy/mens-basketball/.

"How Are Fantasy Basketball Points Calculated?" *Www.rotowire.com*,
www.rotowire.com/faq/how-are-fantasy-basketball-points-calculated-51b51631.

"How to Play Yahoo Fantasy Basketball \|Yahoo Help." *Yahoo.com*, 2026,
help.yahoo.com/kb/SLN6930.html. Accessed 9 Feb. 2026.

Hunter, Vielma. *Picking Winners in Daily Fantasy Sports Using Integer
Programming*. No. 2, 2019,
juan-pablo-vielma.github.io/publications/Picking-Winners.pdf. Accessed 9
Feb. 2026.

Jr NBA. "Basketball Positions." *NBA.com: Jr. NBA*, 23 Sept. 2015,
jr.nba.com/basketball-positions/.

O'Connor, Sean. "Basketball Stats Explained - from Basic to Advanced."
*Sportsvisio.com*, SportsVisio, 16 May 2024,
www.sportsvisio.com/stories/basketball-stats-explained.

"Optimization with PuLP --- PuLP 2.6.0 Documentation."
*Coin-Or.github.io*, coin-or.github.io/pulp/.

Pandas. "Python Data Analysis Library." *Pydata.org*, 2018,
pandas.pydata.org/.

Papageorgiou, George, et al. "An Innovative Method for Accurate NBA
Player Performance Forecasting and Line-up Optimization in Daily Fantasy
Sports." *International Journal of Data Science and Analytics*, 19 Mar.
2024, <https://doi.org/10.1007/s41060-024-00523-y>.

"Position Abbreviations in Fantasy Basketball \| Yahoo Help."
*Yahoo.com*, 2026, help.yahoo.com/kb/SLN6927.html

"Scoring Categories in Fantasy Basketball \|Yahoo Help." *Yahoo.com*,
2026, help.yahoo.com/kb/SLN6928.html. Accessed 9 Feb. 2026.

W3Schools. "Python RegEx." *W3schools.com*, 2019,
www.w3schools.com/python/python_regex.asp.
