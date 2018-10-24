#!/bin/bash

dir=`realpath $1`
cp -R ./linux_client "$dir"
var=$dir/linux_client/spc.sh
echo alias spc="'""bash "$var"""'" | cat >> $HOME/.bashrc
source ~/.bashrc