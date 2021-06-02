# External Package for Rivet 3 analysis in CMS experiment at CERN

This package is a software that provides you the opportunity to make MC event generation using your personal rivet analysis

# Installation

```
export SCRAM_ARCH=slc7_amd64_gcc900
cmsrel CMSSW_11_2_4
cd CMSSW_11_2_4/src
cmsenv
git cms-init -q
git-cms-addpkg GeneratorInterface/RivetInterface
git-cms-addpkg Configuration/Generator
git clone ssh://git@gitlab.cern.ch:7999/cms-gen/Rivet.git
git remote add cms-gen ssh://git@gitlab.cern.ch:7999/cms-gen/Rivet.git
git clone https://github.com/ckamtsikis/External_Rivet3.git
cp /path/to/personal/analysis.cc $CMSSW_BASE/src/External_Rivet3/JetAnalysis/src
cp /path/to/personal/data.yoda $CMSSW_BASE/src/External_Rivet3/JetAnalysis/data
source $CMSSW_BASE/src/External_Rivet3/JetAnalysis/test/source_rivetSetup.sh
scram b -j4
```   
