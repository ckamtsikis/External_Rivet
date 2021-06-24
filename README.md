# External Package for Rivet 3 analysis in CMS experiment at CERN

This package provides you the opportunity to make MC event generation using your personal rivet analysis

# Installation

```
export SCRAM_ARCH=slc7_amd64_gcc820
cmsrel CMSSW_11_1_0
cd CMSSW_11_1_0/src
cmsenv
git cms-init -q
git-cms-addpkg GeneratorInterface/RivetInterface
git-cms-addpkg Configuration/Generator
git clone ssh://git@gitlab.cern.ch:7999/cms-gen/Rivet.git
git remote add cms-gen ssh://git@gitlab.cern.ch:7999/cms-gen/Rivet.git
git clone --branch CMSSW_11_1_0 https://github.com/ckamtsikis/External_Rivet.git
cp /path/to/personal/analysis.cc $CMSSW_BASE/src/External_Rivet/JetAnalysis/src  // Optional
cp /path/to/personal/data.yoda $CMSSW_BASE/src/External_Rivet/JetAnalysis/data   // Optional
source $CMSSW_BASE/src/External_Rivet/JetAnalysis/test/source_rivetSetup.sh
scram b -j8
```   
