# hgc-dqmgui

This repository tracks sparse files of CMS-HGCAL-DQM layouts and rendering plugins for system tests. These code are tracked independently because:

1. It is much easier for mainteinance
2. The code will be modified from time to time to meet the needs in beam tests at different stages
3. The DQM layout for the HGCAL beam tests can be different from the official one
4. Expertise from the CMS DQM experts is required to maintain the code in the official tool

Still, once the HGCAL is about to be deployed in the CMS DQM (somtime in the period of 2023 - 2029), one can consider to create a pull request to merge the files in the official tool `dqm-deployment`.

Below shows instructions on building a dqm-gui (cf. [cms-twiki-DQMGuiForUsers](https://twiki.cern.ch/twiki/bin/viewauth/CMS/DQMGuiForUsers)) and replacing the layouts and rendering plugins for the HGCAL beam test purpose.

## Build DQM GUI

Create your DQMGUI directory. Here it is called tbDQMGUI and install the required packages
```bash
mkdir tbDQMGUI
cd tbDQMGUI
sudo yum -y install git bzip2 perl-Switch perl-Env perl-Thread-Queue libXpm-devel libXmu libXext-devel mesa-libGLU-devel libXinerama libXi libXft-devel libXrandr libXcursor zsh tk perl-ExtUtils-Embed compat-libstdc++-33
```

In a clean environment do:
```bash
/bin/bash
export PATH=$PATH:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin
cd tbDQMGUI
git clone https://github.com/dmwm/deployment.git
```

Go to https://github.com/dmwm/deployment/tags to get the latest tag. (currently using HGC2306a)
```bash
$PWD/deployment/Deploy -A slc7_amd64_gcc630 -r "comp=comp" -R comp@<LATESTTAG> -t MYDEV -s "prep sw post" $PWD dqmgui/bare
```

Put the files workspaces-online.py, HGCalRenderPlugin.cc and hgcal-layouts.py in the following directories
```bash
workspaces-online.py → current/config/dqmgui/
HGCalRenderPlugin.cc → current/config/dqmgui/style/
hgcal-layouts.py → current/config/dqmgui/layouts/
```

We only need HGCAL so we can remove certain files. In style directory keep only utils\* and HGCAL\*
```bash
cd current/config/dqmgui/style
mkdir backup
mv *.* backup/
mv backup/utils.* .
mv backup/HGCalRenderPlugin.cc .
```

The silicon sensor maps are TH2Poly. These are not yet included in DQMGUI ([cms-sw/cmssw#PR41932](https://github.com/cms-sw/cmssw/pull/41932) and [cms-DQM/dqmgui_prod#PR14](https://github.com/cms-DQM/dqmgui_prod/pull/14)). Follow the next steps in order to be able to display the map plots. You will need the files from /afs/cern.ch/user/d/ditsiono/public/DQM_stuff

```bash
cd ~/tbDQMGUI/current/sw/slc7_amd64_gcc630/cms/dqmgui/
cp -r 9.7.8 orig_9.7.8

# Replace the files from the afs directory to your local copy
cp -r </afs/cern.ch/user/d/ditsiono/public/DQM_stuff/new_feature_9.7.8.2/> .
cp -r </afs/cern.ch/user/d/ditsiono/public/DQM_stuff/quick.sh> .

source quick.sh

cd 9.7.8/
cd 128/
mv include/ tmp
rm -r tmp/
cp -r ../../new_feature_9.7.8.2/128/include/ .
```

To start the DQM GUI with “online” flavor:
```bash
cd ~/tbDQMGUI/
source current/apps/dqmgui/128/etc/profile.d/env.sh
$PWD/current/config/dqmgui/manage -f online start "I did read documentation"
```

If you get the error "Unable to perform kinit", please comment block lines related to kerberos in the $PWD/current/config/dqmgui/manage script.

The online flavour listens to port 8070. Once you have started the online GUI you can access it via your browser at:
```
http://hgcdaq00.cern.ch:8070/dqm/online-dev/session/
```

To stop the DQM GUI:
```bash
cd ~/tbDQMGUI/
$PWD/current/config/dqmgui/manage -f online stop "I did read documentation"
```

To upload a root file:
```
visDQMUpload http://hgcdaq00.cern.ch:8070/dqm/online-dev DQM_V0001_HGCAL_R000123481.root
```

General: After every time you log in to the machine, you need to run the following command in order to have access to DQMGUI commands.
```
source current/apps/dqmgui/128/etc/profile.d/env.sh
```

## Reference
- https://twiki.cern.ch/twiki/bin/viewauth/CMS/DQMGuiForUsers
- https://indico.cern.ch/event/1331642/
