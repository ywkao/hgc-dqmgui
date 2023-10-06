# hgc-dqmgui

This repository tracks sparse CMS-HGCAL-DQM layouts and rendering plugins for system tests. These codes are placed in an independent storage instead of the official one because:

1. Expertise from the CMS DQM experts is required to maintain the code in the official tool
2. The code will be modified from time to time to meet the needs of beam tests at different stages
3. The DQM layout for the HGCAL beam tests differs slightly from the official one

Below are instructions on building a DQM GUI for the HGCAL. These commands are based on an official tutorial [[1]](#1), with additional steps for setting up HGCAL DQM. The procedure includes the following four steps:

- Step1: Deploy a dqmgui
- Step2: Update layout and rendering plugins
- Step3: Implement TH2Poly for monitor elements
- Step4: Useful commands (start, stop, and upload DQM files)

Steps 1 to 3 only need to be performed for the first time. Step 4 provides commands for usual maintenance.

Reminder: once the HGCAL is ready for deployment in the CMS DQM (sometime between 2023 and 2029), one can consider creating a pull request to incorporate the files in the official tool [[2]](#2).

## How to build a DQM GUI for the HGCAL beam tests

### Step1: Deploy a dqmgui
Create your DQMGUI directory. Here, it is called tbDQMGUI. Then, install the required packages.
```bash
mkdir tbDQMGUI
cd tbDQMGUI
sudo yum -y install git bzip2 perl-Switch perl-Env perl-Thread-Queue libXpm-devel libXmu libXext-devel mesa-libGLU-devel libXinerama libXi libXft-devel libXrandr libXcursor zsh tk perl-ExtUtils-Embed compat-libstdc++-33
```

In a clean environment, do:
```bash
/bin/bash
export PATH=$PATH:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin
cd tbDQMGUI
git clone https://github.com/dmwm/deployment.git
```

Go to https://github.com/dmwm/deployment/tags to get the latest tag. (e.g. comp@HGC2306a)
```bash
$PWD/deployment/Deploy -A slc7_amd64_gcc630 -r "comp=comp" -R comp@<LATESTTAG> -t MYDEV -s "prep sw post" $PWD dqmgui/bare
```

### Step2: Update layout and rendering plugins
Put the codes in the following directories
```bash
git clone git@github.com:CMS-HGCAL/hgc-dqmgui.git
cp hgc-dqmgui/workspaces-online.py current/config/dqmgui/
cp hgc-dqmgui/HGCalRenderPlugin.cc current/config/dqmgui/style/
cp hgc-dqmgui/HGCalAuxiliaryInfo.h current/config/dqmgui/style/
cp hgc-dqmgui/hgcal-layouts.py current/config/dqmgui/layouts/
cp hgc-dqmgui/quick_replacement.sh current/sw/slc7_amd64_gcc630/cms/dqmgui/ # for Step3
```

We only need HGCAL so we can remove certain files. In the style directory keep only utils\* and HGCAL\*
```bash
cd current/config/dqmgui/style
mkdir backup
mv *.* backup/
mv backup/utils.* .
mv backup/HGCalRenderPlugin.cc .
```

### Step3: Implement TH2Poly for monitor elements
The silicon sensor maps are TH2Poly. These are not yet included in DQMGUI [[3]](#3)[[4]](#4). Use the following commands to implement TH2Poly for displaying polygonal wafer maps. You will need the files from /afs/cern.ch/user/d/ditsiono/public/DQM_stuff

```bash
cd ~/tbDQMGUI/current/sw/slc7_amd64_gcc630/cms/dqmgui/

# Replace the files from the afs directory to your local copy
cp -r </afs/cern.ch/user/d/ditsiono/public/DQM_stuff/new_feature_9.7.8.2/> .

source quick_replacement.sh
```

The `new_feature_9.7.8.2` was created following instructions in [[2]](#2). Relevant links are provided here [[5]](#5)[[6]](#6) in case of a need in the future.

### Step4: Useful commands (start, stop, and upload DQM files)
To start the DQM GUI with an "online" flavor:
```bash
cd ~/tbDQMGUI/
source current/apps/dqmgui/128/etc/profile.d/env.sh
$PWD/current/config/dqmgui/manage -f online start "I did read documentation"
```

If you get the error "Unable to perform kinit", please comment/block lines related to kerberos in the $PWD/current/config/dqmgui/manage script, and then start again.

The online flavour listens to port 8070. Once you have started the online GUI you can access it via your browser at:
```
http://hgcdaq00.cern.ch:8070/dqm/online-dev/session/
```

To stop the DQM GUI:
```bash
cd ~/tbDQMGUI/
$PWD/current/config/dqmgui/manage -f online stop "I did read documentation"
```

Whenever the rendering plugins are updated, to see the rendering effect on the DQM GUI, we need to stop it and then start again so that the rendering plugins are properly compiled.

To upload a root file:
```
visDQMUpload http://hgcdaq00.cern.ch:8070/dqm/online-dev DQM_V0001_HGCAL_R000123481.root
```

General: Every time you log in to the machine, you need to run the following command to access DQMGUI commands.
```
source current/apps/dqmgui/128/etc/profile.d/env.sh
```

## Reference
<ul>
    <li id="#1">[1] https://twiki.cern.ch/twiki/bin/viewauth/CMS/DQMGuiForUsers</li>
    <li id="#2">[2] https://github.com/cms-DQM/dqmgui_prod</li>
    <li id="#3">[3] [cms-sw/cmssw#PR41932](https://github.com/cms-sw/cmssw/pull/41932)</li>
    <li id="#4">[4] [cms-DQM/dqmgui_prod#PR14](https://github.com/cms-DQM/dqmgui_prod/pull/14)</li>
    <li id="#5">[5] https://github.com/cms-DQM/dqmgui_prod/issues/13#issuecomment-1576425471</li>
    <li id="#6">[6] https://github.com/ywkao/dqmgui_prod/tree/th2poly</li>
</ul>
