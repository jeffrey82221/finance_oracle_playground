# finance_oracle_playground
Study the usage of SUA / the-oracle / beibo / empyrial

# Install 


## Setup lightGBM & XGBoost

```
brew install cmake libomp
export LDFLAGS="-L/opt/homebrew/opt/libomp/lib"
export CPPFLAGS="-I/opt/homebrew/opt/libomp/include"
conda create -n boost
conda activate boost
conda install python=3.8.8
conda install numpy scipy scikit-learn
conda install lightgbm
conda install grpcio
pip install pystan==2.19.1.1
pip install prophet
pip install xgboost
```

## Install the-oracle & empyrial & sua
```
pip install the-oracle
pip install empyrial
pip install sua
```

# Start the conda environment 
```
conda activate boost
```
# Tutorial 