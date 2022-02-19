# DREN-Duckies-vs.-Fisches
This is a reproduction project for an artificial busines scenario. This repository includes a large file of a docker image. To clone the completely repository please install the Git Large File Storage with following command:
```bash
sudo apt-get install git-lfs
```
Clone the repositry:
```bash
git clone https://github.com/brt30696/DREN-Duckies-vs.-Fisches.git
```

## Run automatic dispatcher

To start an automated execution of all scripts and generation of the paper run the dispatcher.sh script. This will build the docker container from the Dockerfile, runs it and copies the generated paper out of the container. The generatet .pdf file is copied into the paper directory.

## Run docker container in interactive mode

To run the container in interactive mode please execute following commands:

```bash
docker build -t repro .

docker run -it repro
```

Now a terminal inside the container shows up. To execute the solver please refer to the cli options:

```bash
usage: solver.py [-h] [--profs D F] [--times D F] [--palls D F] [--rubbs N] [--assum D F]

Add the Constraints for the Solver

optional arguments:

  -h, --help           show this help message and exit
  
  --profs D F, -p D F  profit per duck (D), profit per fish (F) (default: [5,4])
  
  --times D F, -t D F  available production time for duckies (D), fishes (F)(default: [400, 300])
  
  --palls D F, -e D F  required pallets per duck (D), fish (F) (default: [100,125])
  
  --rubbs N, -r N      total supplied rubber pallets (N) (default:50000)

  --assum D F, -a D F  assumption for future sales duckies (D), fishes(F)(default: None)
```
  
## Load the docker image 

If you can't build an image from the given Dockerfile you can load an existing image from the given gz.tar file. Run following command:

```bash
docker load < repro_image.tar.gz 
```

To run the image with automated generation run following command:

```bash
docker run --entrypoint ./entrypoint.sh repro 
```

To run the image in interactive mode run following command:

```bash
docker run -it repro 
```
