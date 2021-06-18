# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: External_Rivet3/JetAnalysis/python/QCD_Pt-15To7000_TuneCUETP8M1_Flat_14TeV-pythia8_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10 --python_filename=QCD_Pt-15To6500_TuneCUETP8M1_Flat_13TeV-pythia8_cfg.py --customise=External_Rivet3/JetAnalysis/Pythia8_tuneCUETP8M1_customize.py
import FWCore.ParameterSet.Config as cms
import os
import random
import time

process = cms.Process('GEN')

random.seed(time.time())
rnd1 = random.randint(0, 100000000)
#rnd2 = random.randint(0, 100000000)

job_index = int(10)
#job_index = int(os.getenv("JOBINDEX"))
#seed_gen = 100*job_index+rnd1
#seed_vertex = 100*job_index+rnd2

dataset = os.getenv("LHESET")
files = file(dataset).read().split("\n")
#files = filter(lambda s: s!="", files)
#files = [ os.path.join("rfio:"+files[0], f) for f in files[1:] ]

files_per_job = int(os.getenv("FILESPERJOB"))
file_start = files_per_job*(job_index)
file_end = files_per_job*(job_index+1)
if file_end > len(files):
    file_end = len(files)

files_scoped = files[file_start:file_end]
#files_scoped = files[1:2]
print "Files to read in: ", files_scoped

process.source = cms.Source("LHESource",
                    fileNames = cms.untracked.vstring(*files_scoped),
#                    skipBadFiles = cms.untracked.bool(True)
                    )


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10),
)

#process.RandomNumberGeneratorService.generator.initialSeed = int(os.getenv('seed'))

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('External_Rivet3/JetAnalysis/python/QCD_Pt-15To7000_TuneCUETP8M1_Flat_14TeV-pythia8_cff.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('QCD_Pt-15To7000_TuneCUETP8M1_Flat_14TeV-pythia8_cff_py_GEN.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(				 
        pythia8PowhegEmissionVetoSettings = cms.vstring(
            'POWHEG:veto=1',
            'POWHEG:pTdef=1',
            'POWHEG:emitted=0',
            'POWHEG:pTemt=0',
            'POWHEG:pThard=2', #userhook = 2
            'POWHEG:vetoCount=100',
            'SpaceShower:pTmaxMatch=2',
            'TimeShower:pTmaxMatch=2',
        ),
        processParameters = cms.vstring(
            'Main:timesAllowErrors    = 10000',
            'ParticleDecays:limitTau0 = on',
            'ParticleDecays:tauMax = 10',
            'Tune:pp=14',
            'Tune:ee=7',
            'MultipartonInteractions:pT0Ref=2.4024',
            'MultipartonInteractions:ecmPow=0.25208',
            'MultipartonInteractions:expPow=1.6',
        ),
        parameterSets = cms.vstring('pythia8PowhegEmissionVetoSettings','processParameters')
        )        
)
	

process.ProductionFilterSequence = cms.Sequence(process.generator)
# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

# customisation of the process.

# Automatic addition of the customisation function from External_Rivet3.JetAnalysis.Pythia8_tuneCUETP8M1_customize
from External_Rivet3.JetAnalysis.Pythia8_tuneCUETP8M1_customize import customise 

#call to customisation function customise imported from External_Rivet3.JetAnalysis.Pythia8_tuneCUETP8M1_customize
process = customise(process)
#process.rivetAnalyzer.OutputFile = cms.string(os.getenv('yodafile'))
process.rivetAnalyzer.CrossSection = cms.double(1.000e-09)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
