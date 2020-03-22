# Make sure checkpoint_m_to_d.pth.tar and checkpoint_d_to_m.pth.tar in stored in the logs folder

# ---------------------------------------------------------------------------------------------------------
# Getting results for the best model with duke as source and market as target
python3 main.py -s duke -t market -cs cyclegan -mmd 1 --lmd 0.3 --lmd_ext 0.33  --evaluate --resume logs/checkpoint_d_to_m.pth.tar
mkdir results_duke_to_market
mv *.jpg results_duke_to_market

# ---------------------------------------------------------------------------------------------------------
# Getting results for the best model with market as source and duke as target
python3 main.py -s market -t duke -cs cyclegan -mmd 1 --lmd 0.3 --lmd_ext 0.33  --evaluate --resume logs/checkpoint_m_to_d.pth.tar
mkdir results_market_to_duke
mv *.jpg results_market_to_duke

# ---------------------------------------------------------------------------------------------------------
# Check the folders for the images generated and the terminal for the scores