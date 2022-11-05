# finance_oracle_playground
Study the usage of SUA / the-oracle / beibo / empyrial

# Install 


## Setup environment for empyrial

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
conda install Jinja2
pip install empyrial
pip install xgboost
```
## Setup environment for the-oracle

```
conda create -n oracle
conda activate oracle
conda install python=3.8.8
conda install pytorch==1.8.0
conda install lightgbm
pip install pystan==2.19.1.1
pip install prophet==1.0
pip install darts==0.20.0
pip install the-oracle==0.1.1
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

```
python demo/run.py
```


# TODO: 
- [ ] Fix the-oracle not working problem 
- [ ] Understand the mechanism of empyrial and the-oracle
- [ ] Combine the `return rate` of the-orical with empyrial's profolio optimization