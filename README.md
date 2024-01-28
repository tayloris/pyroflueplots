# pyroflueplots

A compact tool for visualizing data obtained from pyrolysis experiments.

![Customized bar plots](https://github.com/tayloris/pyroflueplots/blob/main/plots/bar_plots.jpg)
![Customized dot plots](https://github.com/tayloris/pyroflueplots/blob/main/plots/dot_plots.jpg)

This facilitates data analysis for the following scientific article
[Industrially relevant pyrolysis of diverse contaminated organic wastes: Gas compositions and emissions to air](https://www.sciencedirect.com/science/article/pii/S0959652623029359)

It is required to have Python, and Git installed.

## Clone the repository:

Open the command windows and type
```
$ cd C:\pathToRepository\
```

Cone the repository
```
$ git clone https://github.com/tayloris/pyroflueplots
```

## First time use:
Create a Python environment and install the packages specified in requirements.txt
```
$ create a python env
```

## Before running a script:
First Activate your Python environment
```
$ C:\PythonEnv\pythonEnv\Scripts\activate.bat
```

Indicate the location of the repository source code
```
$ set PYTHONPATH=%PYTHONPATH%;C:\pathToDirectory\pyroflueplots\src
```
## Run scripts to generate plots:
Go to the repository
```
$ cd C:\pathToDirectory\pyroflueplots\
```

Run an example of a script
```
$ python scripts\examples\autoBarPlotsEm_factors.py
$ python scripts\examples\autoBarPlotsMatrix_mass_balance.py
$ python scripts\examples\autoBarPlotsLoop.py
$ python scripts\examples\autoPlotGF.py
```








For Ubuntu
1) Activate Python enviroment
`$source /pathToPythonEnv/bin/activate` 

2) Indicate the location of the repository source code 
export PYTHONPATH=$PYTHONPATH:/PathToRepo/pyroflueplots/src/
