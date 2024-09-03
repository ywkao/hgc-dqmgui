#!/bin/bash
current="."
destination="/data/srv/current/config/dqmgui"
backup="./backup"

function update(){
    f=$1
    d=$2

    cp -p ${current}/$f $d
    ls -lhrt $d/$f
}

# backup workspaces-online.py
mkdir -p ${backup}
cp -p "/data/srv/current/config/dqmgui/workspaces-online.py" ${backup}

# update rendering plugins for HGCAL DQM plots
update "workspaces-online.py" "${destination}"
update "HGCalRenderPlugin.cc" "${destination}/style"
update "hgcal-layouts.py" "${destination}/layouts"
update "HGCalAuxiliaryInfo.h" "${destination}/style"
