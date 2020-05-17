![alt text](/assets/logo.png "PyXFLR")

# Python API for XFLR5 automation

## state of the project:

Currently having difficulty reliably controlling XFLR through python. Have had some success in automatically creating wings/tails. Project is going through restructure so nothing works.


## Explanation:

XFLR is  a great tool for low reynolds number analysis of UAVs but iterating through designs is a long process. PyXFLR automates the design iteration process, allowing easy analysis of infinite design possibilities and capturing the results to find the most optimal solution.

Pyxflr currently works on the bases of pressing keys. I'm researching ways of controlling it through https://automatetheboringstuff.com/chapter18/ and https://pywinauto.github.io/ 


## Requires:

- XFLR5                 http://www.xflr5.tech/xflr5.htm

- ahk python library    https://pypi.org/project/ahk/


## Features:

- [ ] Create foils
- [ ] Analyse foils
- [ ] Create plane configurations
- [ ] Create analysis methods
- [ ] Analyse plane configurations and save results to file
