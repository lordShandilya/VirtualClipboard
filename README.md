# VirtualClipboard
This project aims at making it is easy to store passwords and snippets with just your command line.


## How to use
- Clone this repository on your system.
```
git clone https://github.com/lordShandilya/VirtualClipboard
```
- Install dependencies.
```
cd VirtualClipboard
pip install -r requirements.txt
```
- Now copy any text on your clipboard and go to the folder in your terminal where you have cloned the repo and type:
```
python main.py put
```
- The command line will ask for a key and then it will be saved in a json file.
- To get it all you have to do is type this in the command line:
```
python main.py get
```
- Now it will ask for a key, give the one you set before.
- And whatever you saved will be automatically copied to your clipboard.
- If you want to see all your saved clippings just type:
```
python main.py show
```
