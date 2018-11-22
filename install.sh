#!/bin/bash

dir=`realpath $1`
cp -R ./linux_client "$dir"
var=$dir/linux_client/spc.sh
echo alias spc="'""bash "$var"""'" | cat >> $HOME/.bashrc
source ~/.bashrc
sudo cp ./linux_client/spc_man /usr/local/man/man1/spc.1
sudo gzip /usr/local/man/man1/spc.1
