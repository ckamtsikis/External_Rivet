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

    DEFAULT_RIVET_ANALYSIS_CTOR(Ratios_InclusiveJets_XSection);

    // ---------- Book Histograms -------------
    void init() {

      FinalState fs;
      FastJets akt(fs, FastJets::ANTIKT, 0.8);
      declare(akt, "antikT");

      // Book Inclusive Jets
      book(_h_Inclusive2jets,1,1,1);
      book(_h_Inclusive3jets,2,1,1);
      book(_h_Inclusive4jets,3,1,1);
      book(_h_Inclusive5jets,4,1,1);

      // Book Ratios
      book(_h_Ratio32,5,1,1);
      book(_h_Ratio43,6,1,1);
      book(_h_Ratio54,7,1,1);
      book(_h_Ratio42,8,1,1);
      book(_h_Ratio53,9,1,1);
      book(_h_Ratio52,10,1,1);
      
    }

    //-------- Per-event Analysis -----------
    void analyze(const Event& event) {
      const Jets& jets = apply<JetAlg>(event, "antikT").jetsByPt( Cuts::absrap < 2.5 && Cuts::pT >= 100.*GeV );

      //-------------- At least 2 jets --------------------
      if(jets.size() < 2) vetoEvent;
      if(jets[0].pT() < 150.*GeV) vetoEvent;
      
      double ht2 = 0.5*(jets[0].pT()+jets[1].pT());
      _h_Inclusive2jets->fill(ht2/GeV);

      //------------------ Extra Jets ---------------------
      if(jets.size() >= 3) _h_Inclusive3jets->fill(ht2/GeV);
      if(jets.size() >= 4) _h_Inclusive4jets->fill(ht2/GeV);
      if(jets.size() >= 5) _h_Inclusive5jets->fill(ht2/GeV); 
      
    }

    //--------- Normalize histograms -----------
    void finalize() {
      
      // Ratios R32 R43 R42 booking and calculation
      divide(_h_Inclusive3jets, _h_Inclusive2jets, _h_Ratio32);
      divide(_h_Inclusive4jets, _h_Inclusive3jets, _h_Ratio43);
      divide(_h_Inclusive5jets, _h_Inclusive4jets, _h_Ratio54);
      divide(_h_Inclusive4jets, _h_Inclusive2jets, _h_Ratio42);
      divide(_h_Inclusive5jets, _h_Inclusive3jets, _h_Ratio53);
      divide(_h_Inclusive5jets, _h_Inclusive2jets, _h_Ratio52);

      // scale the cross sections histograms
      scale(_h_Inclusive2jets, crossSection()/picobarn/sumOfWeights());
      scale(_h_Inclusive3jets, crossSection()/picobarn/sumOfWeights());
      scale(_h_Inclusive4jets, crossSection()/picobarn/sumOfWeights());
      scale(_h_Inclusive5jets, crossSection()/picobarn/sumOfWeights());

    }

    Histo1DPtr _h_Inclusive2jets, _h_Inclusive3jets, _h_Inclusive4jets, _h_Inclusive5jets;
    Scatter2DPtr _h_Ratio32, _h_Ratio43, _h_Ratio54, _h_Ratio42, _h_Ratio53, _h_Ratio52;

  };

  // The hook for the plugin system
  DECLARE_RIVET_PLUGIN(Ratios_InclusiveJets_XSection);
}
