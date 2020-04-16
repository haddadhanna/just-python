from pathlib import Path

#path = Path("Exercices\mypackage1")
#print(path.exists())
#path.rmdir()
#path.mkdir()

path = Path("mypackage")
for file in path.glob('*'):
    print(file)

