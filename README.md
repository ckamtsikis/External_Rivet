# External Package for Rivet 3 analysis

This package is a software that provide you the opportunity to add your personal rivet analysis and make a MC event generation

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
source $CMSSW_BASE/src/GeneratorInterface/RivetInterface/test/rivetSetup.sh
source Rivet/rivetSetup.sh
scram b
```   
