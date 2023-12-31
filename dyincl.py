import ROOT
from args import args
from make_files import make_files

dir_kwargs = {
    "mc_dir": "/gpfs/ddn/srm/cms//store/mc",
    "prod_camp": "RunIISummer20UL18NanoAODv9",
    "sample": "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8",
    "nano": "NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2",
    "flash_dir": "/scratchnvme/cattafe/FlashSim",
}

obj_list = ["Electron", "Electron_fromJets", "Muon", "Jet"]


make_files(obj_list, args, **dir_kwargs)
