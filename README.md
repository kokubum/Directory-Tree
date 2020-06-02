# Directory Tree Generator
Script made with python 3 to generate a directory tree of some path.

## Getting Started

Clone this repository:

```
git clone https://github.com/kokubum/Directory-Tree.git
```

### Running

Installing the PIL library:
```
python3 -m pip install --upgrade Pillow
```
Run the script:
```
python3 run.py
```
## Example

**Input:**
  * Path to the folder that you want to use as base directory.

**Output:**
  * .txt file with the generated tree.
```  
  |TreeGen
  |─────file2.txt
  |─────file.txt
  |─────subdirectory2
       |─────file2.txt
       |─────file.txt
       |─────subdirectory1
  |─────subdirectory1
       |─────file2.txt
       |─────file.txt
 ```
  * Optional .png file with the same tree.
  
  
