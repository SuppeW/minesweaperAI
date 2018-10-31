I will attempt to make a minewseaper AI.

With no knowledge about making either an AI, nor neural networks, or any other form of
machine learning algorithms. I will go trough multiple examples trying to piece together
the puzzle and hopefully in the end I will end up with a version I am happy with.

-- Written by Anders Leonard Wøien.
-- Start date: 29.10.2018.


First of I wanna make a minesweaper board, and see if I can replicate the games mechanics.
I am going to be using python for this and I am think only a terminal based example for now.
The visual stuff will come later.

Key game mechanics:
- Grid has x * y cells.
- Every cell has a: state, bomb, not bomb, empty, a neighboring bomb state.
- For every neighboring bomb in an empty cell, a number will display the amount of bombs.
- The first cell you click on will never be a bomb.
- If a empty cell with no neighbors is clicked, all other neighboring cells, will open as well.
- Cells that are not open, have one of three states, flagged, active and '?'.
- inputs of the board size and the amount of bombs should be displayed at the beginning.


How to make the board:
- I am thinking of making up the board using multiple 2D arrays/lists, one list for the
  the active cells board where. This will represent every cell that has not been
  opened yet. This will have a value of: Active or Dead.
  The second List will contain all bombs. This list will only be used to set up the
  actual playing board, that will be the third list, containing all bombs, numbers
  and empty cells. --- The second list will only be used for calculating purposes. I bet
  there is a better way to go about this, if you think of anything. Let me know, for now
  I will stick with this ---

- Naming the lists:
    liveCells = [[]] //This will only tell whether the current cell has been opened.
    bombCells = [[]] //This will randomize the board with bombs.
    gameCells = [[]] //This will contain all numbers, and bombs.

- The game stops when either all bomb have been found so, or you press a liveCell
  with a bombCell behind it.



- bombCells:
    To spread out the amount of bombs on the board, I will randomize which cell
    should be given a bomb value first. Because there is more bombs then 50% of
    total numbers of cells, running the for loop normally will group up all the bombs
    in the top right corner, considering there is a 50% chance of a cell being a bomb
    or not. --- DISCLAIMER, there is also probably a better way to do this, but for now
    this is the only way I can think of to keep the total number of bombs be the same as
    the inputted bombAmount.

    I am not getting the method above to work, because the list cells have a chance of
    being overwritten, and replacing a bomb, this causes the total number of bombs to
    be incorrect. I have also been trying to look at other open source minesweaper games
    to see how they have done it, but I cant seem to understand it. At the point I am
    just trying to wrap my head around a new method to build the minefield.

    After tinkering around for a bit, I think I have found a way to make the gird
    store the value of 0 or 1. This is by first filling up the bombCells list with
    zeros, for then later to randomly fill the grid with 1s replacing the zeros.
    I am running into a couple of errors here and there, but I think I am no the
    right path.

    I have now managed to implement the random selection of bomb cells,
    the problem of overwriting already placed bombs is still there.
    atm I have an idea of how on how to fix this, however, it includes making a temporary
    list of placed bombs, and checking the main list towards this one, however, this seems
    like unnecessarily much work, and I am browsing the net for better ways. I think there
    is a way to generate a new number every time you call the random function.
    SOLUTION: I solved the problem by simply checking if the current random cell already
    had a value of 1, and put everything inside a while True loop, and only breaking it
    when the random value found a free cell. This means, it will try to find a free cell
    on and on, until it finds one.

    The game grid has now had its first test run, and worked as I expected. Next step on
    the agenda will be to implement then numbers and empty cells list. As mentioned
    previously, this will be a sperate 2D list, fetching the bomb cells from the
    randBomb function.

    To calculate the neighbors I will run the list trough a nested for loop, looking for
    the value of 1 in every neighboring cell, this goes trough ever cell of the entire
    grid. I also will have to implement rules that does not allow to check neighbors
    outside the border of the grid. For the empty cells I will change their value to
    E, and the number of adjestent neighboring bomb I will just represent their cell with
    a number. This bumps into a problem where I have put the active bomb cells into
    the value of 1, and will have to change that to something like B, for bomb.

    My current method of checking neighbors for a bomb seems to be working, but I
    have to tweak the settings to be able to get it right, It looks like it clearly sees
    where the bombs are located, but cant really count it to well. I dont know what is
    causing the problem at the moment, but hopefully it has something to do with how
    I set up counting of the neighboring cells, and maybe it is missing a negative number
    something like that. If this does not work, I will work towards a new method,
    however I don't think the current method, containing 13 if statements is the best way
    to go about this. Although, I don't want to check in on other projects because of the
    learning experience, I think I might do so very soon. Reading trough those 13 if
    statements, are not only making me disgusted, because I hate spaghetti, but it is also
    driving me crazy!!

    Ok, so I am finally done making the full playboard, and everything runs just fine.
    Instead of make two different boards, I am now just converting the bombs list,
    to contain both the numbers and bombs for. All the wall and corner rules work flawlessly,
    and the game is also scalable, whit options of grid size and bomb amount at the Start
    of the program.

    The GUI. I will be using pygame to make the playing grid. And with that said,
    Time to get to work! At the moment I am just working my way in, by testeing out
    different functions in pygame. I have made some simple keypress programs, and
    drawn some shapes, my next thing to do, will be to make a grid of rectangles.
    with each rectangle having an id, so I can call i trough my minesweaper function.

    I have now made a working pygame grid, with grey cells, and when the cell i clicked
    It will turn red. I reall had to squeak every part of the code to make it work,
    but in the end, I turned out perfect. Every cell is 19px wide and tall, and every
    cell have a margin of 1. There is still some bugs, when resizing the board, and
    changing the dimensions of the cells. The grey cells line up perfect, but the
    red cells, are misplaced when activated. So I have to figure out this later.
    For now, what remains, is to return a value iterating 1s, so that I can chnage
    the item in the selected game grid. But this should be piece of cake, compared
    to what I have just been trough. Maths is hard...
    Aaaaand, I am done with the cellid, in code called cellnr, to not get confused
    if I ever was to use the built in python-function "id".
