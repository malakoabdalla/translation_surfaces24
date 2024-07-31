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
`sage -pip install sage-flatsurf`
`sage -pip install surface dynamics`

https://flatsurf.github.io/sage-flatsurf/examples/defining_surfaces.html
https://flatsurf.github.io/sage-flatsurf/examples/defining_surfaces.html
### these links are the same 


## To run the notebook
In a terminal run:
`sage -n jupyter`
copy the localhost:8888 url from the kernel terminal output and paste it into VSCode when it asks you what jupyter kernel to use (select the one named Sage)


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
`git status` - checks what's going on with git
`git pull` 

At the end of the day:
`git add -A`
`git commit -m "your message here"`
`git push`

# To run on the research servers
Run

`ssh -t -L 58762:localhost:58762 YOURUSERNAME@magma2.math.wisc.edu sage -n jupyter --no-browser --port-retries 0 --port=58762`

and use your Math IT credentials to log in. Then copy the http://localhost:58762... url that it gives you into VSCode. 


