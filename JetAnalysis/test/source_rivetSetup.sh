#!/bin/bash
source $CMSSW_BASE/src/Rivet/rivetSetup.sh
source $CMSSW_BASE/src/GeneratorInterface/RivetInterface/test/rivetSetup.sh
export RIVET_REF_PATH=$RIVET_REF_PATH:$CMSSW_BASE/src/External_Rivet3/JetAnalysis/data
export RIVET_INFO_PATH=$RIVET_INFO_PATH:$CMSSW_BASE/src/External_Rivet3/JetAnalysis/data
export RIVET_PLOT_PATH=$RIVET_PLOT_PATH:$CMSSW_BASE/src/External_Rivet3/JetAnalysis/data

