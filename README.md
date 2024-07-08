# Install

## VSCode 
This is the text editor we will use to modify and run code. To install follow the instructions at 

## Sage
This is a combination of Python and a bunch of math specific Python libraries. To install, follow the instructions at https://www.sagemath.org/
Run the optional setup step at the end to make sure Sage is added to your terminal path. To make sure this was successful run
`sage -v`
If you get a number, it worked. If you get an error, you need to make sure Sage is added to your terminal path. 

## X Code
Install X Code to get all the build tools for flatsurf:
https://developer.apple.com/xcode/ (Make sure your operating system is up to date first)


## Flatsurf 
Install flatsurf directly into sage by running
`sage -pip install surface dynamics`

https://flatsurf.github.io/sage-flatsurf/examples/defining_surfaces.html
https://flatsurf.github.io/sage-flatsurf/examples/defining_surfaces.html


## To run the notebook
In a terminal run:
`sage -n jupyter`

## Markdown reference
https://www.digitalocean.com/community/markdown

## Tools
Python
Jupyter Notebook
Sage
Flatsurf

## Terminal basics
`pwd` - check what directory you're currently in
`ls` - list all folders and files in the current folder
`cd folder-name` - move into that directory 

## Git instructions
In the terminal, in the folder for the project (check that with `pwd`)
Before you make changes to a fresh branch
`git pull` 

At the end of the day:
`git add -A`
`git commit -m "your message here"`
`git push`

