import ROOT
from args import args
from make_files import make_files

dir_kwargs = {
    "mc_dir": "/gpfs/ddn/srm/cms//store/mc",
    "prod_camp": "RunIISummer20UL18NanoAODv9",
    "sample": "DYJetsToLL_LHEFilterPtZ-0To50_MatchEWPDG20_TuneCP5_13TeV-amcatnloFXFX-pythia8",
    "nano": "NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/",
    "flash_dir": "/scratchnvme/cattafe/FlashSim",
}

obj_list = ["Electron", "Electron_fromJets", "Muon", "Jet"]


make_files(obj_list, args, **dir_kwargs)
