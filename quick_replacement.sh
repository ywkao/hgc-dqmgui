#!/bin/bash
# script to be executed under current/sw/slc7_amd64_gcc630/cms/dqmgui/

dir="9.7.8"
ori_dir="original_9.7.8"
new_dir="new_feature_9.7.8.2"

function copy()
{
    file=$1
    echo "cp ${new_dir}/${file} ${dir}/${file}"
    cp ${new_dir}/${file} ${dir}/${file}
}

function copy_dir()
{
    file=$1
    echo "cp -r ${new_dir}/${file} ${dir}/${file}"
    cp -r ${new_dir}/${file} ${dir}/${file}
}

# backup original directory first
echo "cp -r $dir $ori_dir"
cp -r $dir $ori_dir

# update files for implementing TH2Poly
copy 128/bin/DQMCollector
copy 128/bin/visDQMIndex
copy 128/bin/visDQMRender
copy 128/lib/python2.7/site-packages/Monitoring/DQM/Accelerator.so
copy 128/lib/libDQMGUI.so

# replace the include directory
echo "mv ${dir}/128/include ${dir}/128/tmp"
mv ${dir}/128/include ${dir}/128/tmp
copy_dir 128/include

echo ">>> finished!"
