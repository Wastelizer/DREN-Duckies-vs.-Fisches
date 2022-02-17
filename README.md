# DREN-Duckies-vs.-Fisches
this is a reproduction project for an artificial busines scenario.

to start an automated execution of all scripts and generation of the paper run the dispatcher.sh script.
This will build the docker container, runs it and copies the generated paper out of the container.


to run the container in interactive mode execute following commands:

docker build -t repro .

docker run -it repro

## run docker in interactive mode

You can run the docker container in interactive mode to execute the python solver manualy.


please refer to the cli options:

usage: solver.py [-h] [--profs D F] [--times D F] [--palls D F] [--rubbs N] [--assum D F]

Add the Constraints for the Solver

optional arguments:

  -h, --help           show this help message and exit
  
  --profs D F, -p D F  profit per duck (D), profit per fish (F) (default: [5,4])
  
  --times D F, -t D F  available production time for duckies (D), fishes (F)(default: [400, 300])
  
  --palls D F, -e D F  required pallets per duck (D), fish (F) (default: [100,125])
  
  --rubbs N, -r N      total supplied rubber pallets (N) (default:50000)

  --assum D F, -a D F  assumption for future sales duckies (D), fishes(F)(default: None)
