#! /bin/bash

bold=$(tput bold)
normal=$(tput sgr0)

#Black        0;30     Dark Gray     1;30
#Red          0;31     Light Red     1;31
#Green        0;32     Light Green   1;32
#Brown/Orange 0;33     Yellow        1;33
#Blue         0;34     Light Blue    1;34
#Purple       0;35     Light Purple  1;35
#Cyan         0;36     Light Cyan    1;36
#Light Gray   0;37     White         1;37

NC='\033[0m' # No Color
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'

# функции стадий для pipeline

dump_result() {

	if [ $1 -eq 0  ]
	then
	        printf "${BLUE}${bold} Done. ${normal}${NC}\n"
	else
		printf "${RED}${bold} FAIL. errno($1) ${normal}${NC}\n"
	fi

}

stage_model_preprocessing() {
        printf "${BLUE}${bold} Stage 1. Model preprocessing ${normal}${NC}\n"

	python3 model_preprocession.py

        dump_result $?

}

stage_data_creation() {
        printf "${BLUE}${bold} Stage 2. Data creation ${normal}${NC}\n"

        python3 data_creation.py

        dump_result $?
}

stage_model_preparation() {

        printf "${BLUE}${bold}  Stage 3. Model preparation ${normal}${NC}\n"

	python3 model_preparation.py

        dump_result $?

}

stage_model_testing() {

        printf "${BLUE}${bold}  Stage 4. Model testing ${normal}${NC}\n"

	python3 model_testing.py

        dump_result $?

}

# Функция запуска всех стадий последовательно

stage_full() {

	printf "${BLUE}${bold} Run full stages ${normal}${NC}\n"

	stage_model_preprocessing $@
	stage_data_creation $@
  	stage_model_preparation $@
  	stage_model_testing $@

	dump_result $?

}

printf "${BLUE}${bold} Welcome MLOps pipeline ${normal}${NC}\n"

# Проверка аргументов командной строки

if [ -z $1  ]
then
	stage='full'
else
	stage=$1
fi

# Выбор стадии или запуск всего

case "$stage" in
	"model_preprocession" | '1') stage_model_preprocessing $@ ;;
        "data_creation" | '2') stage_data_creation $@ ;;
	"model_preparation" | '3') stage_model_preparation $@ ;;
	"model_testing" | '4') stage_model_testing $@ ;;
	*) stage_full $@ ;; 
esac


