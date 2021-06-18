#!/bin/bash 
#o
#e

cd /afs/cern.ch/work/c/ckamtsik/private/Analysis/Rivet/NPs/Pythia8/CMSSW_11_2_4/src/test/CUETM1/MPIHADon
eval `scramv1 runtime -sh`
source $CMSSW_BASE/src/Rivet/rivetSetup.sh

cmsRun rivet_InclusiveJets_QCD_Pt-15To7000_TuneCUETP8M1_Flat_13TeV-pythia8_cfg.py
