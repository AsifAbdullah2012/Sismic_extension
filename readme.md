# Thesis: Exploration of Statechart Automata for Variable Structure Systems

## Use python 'Sismic' library

Sismic is mainly developed by Dr. Alexandre Decan as part of his research activities at the Software Engineering Lab of the University of Mons. Sismic is released as open source under the GNU Lesser General Public Licence version 3.0 (LGPLv3).

▶   A python library
▶ Support Harel state chart semantics
▶ Interpreter follows SCXML 1.0 semantics
▶ Follows step execution


## Variability at run-time
a total of 4 changes can be requested at run-time
- State addition
- State remove
- Transition addition
- Transition remove

A state can be Basic, Compound and Final. 

#### State Addition Inputs 
• type ('B' -- basic, 'C' -- Compound, 'F'--Final)(mendatory field)
• name (mendatory field)
• on entry (Optional field)
• on exit (Optional field)
• parent (mendatory field) 
• initial (mendatory field for Compound state addition)

#### State Removal Inputs 
• name (mendatory field)

#### Transition Addition/Removal Inputs
• source (mendatory field)
• target (mendatory field)
• event (Optional field)
• guard (Optional field)
• action (Optional field)
• priority (Optional field)





## Installation
- **virtual environment:** Create python virtual environment, activate it
- **Use this repository** Pull this repository
- **Install dependency** On the virtual environment install dependency

## Run
- run the sismic_test.py file 
- Follow the CLI




