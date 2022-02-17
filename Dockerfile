
# Docker container for a reproduction package for the artificial business
# scenario "Duckies vs. Fishes in cotext of the portfolio exame in 
# reprodusibility engineering

# Copyright 2021, Sebastian Sippl <sebastian.sippl@st.oth-regensburg.de>
# Copyright 2021, Thomas Brandl  <thomas.brandl@st.oth-regensburg.de>
# SPDX-License-Identifier: MIT-0

# Start off of a long-term maintained base distribution
FROM ubuntu:20.04

MAINTAINER Sebastian Sippl <sebastian.sippl@st.oth-regensburg.de>

ENV DEBIAN_FRONTEND noninteractive
ENV LANG="C.UTF-8"
ENV LC_ALL="C.UTF-8"

# Install required packages
RUN apt-get update && apt-get install -y --no-install-recommends \
		nano \
		python3 \
		python3-pip \		
		sudo \
		texlive-base \
		texlive-fonts-recommended \
		texlive-latex-extra \
		texlive-publishers 

# Add user
RUN useradd -m -G sudo -s /bin/bash repro && echo "repro:repro" | chpasswd
USER repro
WORKDIR /home/repro


#install required python modules
RUN pip3 install matplotlib

#copy data into container
ADD --chown=repro data ./data
ADD --chown=repro source ./source
ADD --chown=repro paper ./paper
ADD --chown=repro ./entrypoint.sh .

#add permissions to the files
USER root
RUN chmod -R 775 ./data
RUN chmod -R 775 ./source
RUN chmod -R 775 ./paper
USER repro
