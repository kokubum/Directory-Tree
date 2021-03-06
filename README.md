# Directory Tree Generator
Script made with python 3 to generate a directory tree of some path.

## Getting Started

Clone this repository:

```
git clone https://github.com/kokubum/Directory-Tree.git
```
If you don't have the PIL library:
```
python3 -m pip install --upgrade Pillow
```
### Running

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
  
![tree](https://user-images.githubusercontent.com/47634578/83577703-4b040780-a50b-11ea-91a7-dec31a5cc960.png)
  
