#!/bin/bash
for file in */*.eps
do
    echo -e "Converting ${file} \n"
    epstopdf ${file}

done
