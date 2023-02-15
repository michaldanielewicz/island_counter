# Island counter

### Description

At the beginning of this task, you are given a path to the file that denotes a
two-dimensional array which visualizes a map. Each element of this array will take
one of the following values:
* 0 (which represents water),
* 1 (which represents land).  

These values will form islands on water.

For example:  
0 0 0 0 0 0 0 0 0  
0 1 0 0 0 0 0 0 0  
1 1 1 0 0 0 1 0 0  
1 1 0 0 0 1 1 1 0  
0 0 0 0 0 1 1 0 0  
0 0 1 0 0 0 0 0 0  
1 1 0 0 0 0 0 0 0  
0 0 0 0 0 1 1 0 0  

This example illustrates 4 islands. Counting from left upper corner:
* First Island is made of six land elements,
* Second Island is also made of six land elements,
* Third island consists of 3 elements,
* The last one is made of two elements.

The invocation of your bash script will look like:  

    ./your_script.sh <path_to_the_file>  

where the file denoted by the path will be a text file with only zeros 
(ASCII character 48) and ones (ASCII character 49) and end-of-line, i.e.:

000000000  
010000000  
111000100  
110001110  
000001100  
001000000  
110000000  
000001100  

Write a short program, which will count the number of islands. The following data
structure could be varying in size. The only output of the program written to STDOUT
should be the number (all additional diagnostics information, if needed, should be
written to STDERR).

Example invocation (and output):

    $ ./your_script.sh islands.txt
    4

Take into the assumption, that data structure given to you could be very large in size,
so beware of implementation that could result in stack overflow or out of memory
exception.

### Stack

* Python 3.10

### Requirements

* Docker

### Installation

0. Install Docker.  


1. Clone the repository

   `git clone https://github.com/michaldanielewicz/island_counter`


2. Change directory to the cloned repository

   `cd island_counter`


3. Build the Docker image:

   `docker build -t island_counter .`


### Usage

Run the script by typing into command line:

   `docker run island_counter <FILEPATH>`

e.g. you can use `test_input.txt` for input by typing: 

   `docker run island_counter test_input.txt`
   
In order to run another input you need to copy file to `/island_counter` and re-build Docker image.

### Development / testing

The project uses `Poetry` for dependency management.  
If you have Poetry you can activate virtual env by typing: `poetry shell`
in a project dir.  

You can also run script by typing: `poetry run python main.py <FILEPATH>` -- even without activating env.

To run tests type: `poetry run pytest .`