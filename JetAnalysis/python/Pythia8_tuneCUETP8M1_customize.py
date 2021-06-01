import FWCore.ParameterSet.Config as cms

def customise(process):
        process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
        process.rivetAnalyzer.AnalysisNames = cms.vstring('Ratios_InclusiveJets_XSection')
        process.rivetAnalyzer.OutputFile = cms.string('QCD_Inclusive_Jets_AK8_13TeV.yoda')
        process.rivetAnalyzer.CrossSection = cms.double(1.995e+09)
        process.generation_step+=process.rivetAnalyzer
        process.schedule.remove(process.RAWSIMoutput_step)
        return(process)
