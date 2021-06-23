// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Projections/FinalState.hh"
#include "Rivet/Projections/FastJets.hh"
#include "Rivet/Projections/DressedLeptons.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "Rivet/Projections/PromptFinalState.hh"

namespace Rivet {


  class Ratios_InclusiveJets_XSection : public Analysis {
  public:

    Ratios_InclusiveJets_XSection() : Analysis("Ratios_InclusiveJets_XSection") {}

    // ---------- Book Histograms -------------
    void init() {

      FinalState fs;
      FastJets akt(fs, FastJets::ANTIKT, 0.8);
      addProjection(akt, "antikT");

      // Book Inclusive Jets
      _h_tmp_Inclusive2jets = bookHisto1D("Inclusive2jets");
      _h_tmp_Inclusive3jets = bookHisto1D("Inclusive3jets");
      _h_tmp_Inclusive4jets = bookHisto1D("Inclusive4jets");
      _h_tmp_Inclusive5jets = bookHisto1D("Inclusive5jets");

    }

    //-------- Per-event Analysis -----------
    void analyze(const Event& event) {
      const double weight = event.weight();
      const Jets& jets = applyProjection<JetAlg>(event, "antikT").jetsByPt( Cuts::absrap < 2.5 && Cuts::pT >= 100.*GeV );

      //-------------- At least 2 jets --------------------
      if(jets.size() < 2) vetoEvent;
      if(jets[0].pT() < 150.*GeV) vetoEvent;
      
      double ht2 = 0.5*(jets[0].pT()+jets[1].pT());
      _h_tmp_Inclusive2jets->fill(ht2,weight);

      //------------------ Extra Jets ---------------------
      if(jets.size() >= 3) _h_tmp_Inclusive3jets->fill(ht2,weight);
      if(jets.size() >= 4) _h_tmp_Inclusive4jets->fill(ht2,weight);
      if(jets.size() >= 5) _h_tmp_Inclusive5jets->fill(ht2,weight); 
      
    }

    //--------- Normalize histograms -----------
    void finalize() {

      // scale the cross sections histograms
      scale(_h_tmp_Inclusive2jets, crossSection()/picobarn/sumOfWeights());
      scale(_h_tmp_Inclusive3jets, crossSection()/picobarn/sumOfWeights());
      scale(_h_tmp_Inclusive4jets, crossSection()/picobarn/sumOfWeights());
      scale(_h_tmp_Inclusive5jets, crossSection()/picobarn/sumOfWeights());

    }

    Histo1DPtr _h_tmp_Inclusive2jets, _h_tmp_Inclusive3jets, _h_tmp_Inclusive4jets, _h_tmp_Inclusive5jets;

  };

  // The hook for the plugin system
  DECLARE_RIVET_PLUGIN(Ratios_InclusiveJets_XSection);
}
