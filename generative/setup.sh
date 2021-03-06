#!/bin/bash
#setup script. sets up and activates venv, installs requirements, preprocesses dataset

display_usage() {
	echo "supply data directory as argument"
	echo "\nUsage: $0 [data directory (somthing like ./data/ArtchDaily-Share/] \n"
	}
# if less than two arguments supplied, display usage
	if [  $# -le 1 ]
	then
		display_usage
		exit 1
	fi

# check whether user had supplied -h or --help . If yes display usage
	if [[ ( $# == "--help") ||  $# == "-h" ]]
	then
		display_usage
		exit 0
	fi

virtualenv .venv-arch && source .venv-arch/bin/activate
pip3 install -r ./stylegan2/requirements.txt
python3 preprocess.py $1 
