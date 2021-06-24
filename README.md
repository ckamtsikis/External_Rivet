# External Package for Rivet 3 analysis in CMS experiment at CERN

This package provides you the opportunity to make MC event generation using your personal rivet analysis

# Installation Rivet2

```
export SCRAM_ARCH=slc7_amd64_gcc630
cmsrel CMSSW_9_2_13
cd CMSSW_9_2_13/src
cmsenv
git cms-init -q
git-cms-addpkg GeneratorInterface/RivetInterface
git-cms-addpkg Configuration/Generator
git clone ssh://git@gitlab.cern.ch:7999/cms-gen/Rivet.git
git clone --branch CMSSW_9_2_13 https://github.com/ckamtsikis/External_Rivet3.git
cp /path/to/personal/analysis.cc $CMSSW_BASE/src/External_Rivet3/JetAnalysis/src  // Optional
cp /path/to/personal/data.yoda $CMSSW_BASE/src/External_Rivet3/JetAnalysis/data   // Optional
source $CMSSW_BASE/src/External_Rivet3/JetAnalysis/test/source_rivetSetup.sh
scram b -j8
```   
