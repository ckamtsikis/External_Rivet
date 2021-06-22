#!/bin/bash 

cd afspath                                   # to be set from run_condor.sh script
eval `scramv1 runtime -sh`                   # this is the cmsenv
source $CMSSW_BASE/src/External_Rivet3/JetAnalysis/test/source_rivetSetup.sh

cmsRun cfg.py                                # to be set from run_condor.sh script
