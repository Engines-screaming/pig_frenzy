# Pig Frenzy Game

A game for my girlfriend as a fun project.

# Setting Up Enviroment
Setup a virtual environment with conda and activate it:
```
conda create --name pig_frenzy python=3.7
conda activte pig_frenzy
```

Then to run script:
```
python hungry_pig.py
```

# Exporting to exe with pyinstaller
Since there are extra data files that pig_frenzy relies on, we use the following:
```
pyinstaller --add-data sounds;sounds --add-data imgs;imgs --noconsole pig_frenzy.py -y
```
The --add-data arguments will let us import the sound and image files that we are missing. The --noconsole argument removes the terminal that runs with the program.
