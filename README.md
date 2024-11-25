# CFD_GA_OPT
## Introduction
This program developed a method to optimize the supply air flow rate and temperature by combine CFD with Modelica model. The calculate method could achieve:

*    Combine a simplified CFD model of a room with a Modelica model of a reverse Brayton cycle to deliver air produced by the reverse Brayton cycle as fresh air input to the room.
*    Optimize the supply air volume and temperature using a genetic algorithm to minimize room pollutant concentration, air supply flow rate, and system energy consumption.

## Implemention
### Machine environment
You have to get the below preparations on your machine:
*    Fluent (**Not** less than version 2015_1)
*    Dymola or OpenModelica
*    .msh file that could be used in Fluent

### Case we used in this project
*    The reverse Brayton cycle we developed in Modelica is:
![Modelica files](https://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/modelica.jpg)
*    The room model we developed in Fluent is:
![CFD files](https://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/msh.jpg)
*    The CFD simulation data has been validated, and the simulation results are as follows:
![CFD validation](https://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/valdition.jpg)

*    The Modelica simulation data has been validated, and the simulation results are as follows:
![Modelica validation1](https://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/flowrate.jpg)
![Modelica validation2](https://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/temp.jpg)

### Result
The simulation result was shown below:
We utilized a genetic algorithm to rapidly simulate various design parameters. The variations in velocity and pollutant distribution within the room under different supply air temperatures and velocities are shown in the figure：
*     velocity:
![velocity](https://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/velocity.gif)
*     dpm:
![dpm](http://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/dpm.gif)

*    The final design point and the Pareto front is shown below:
![opt](http://github.com/wenzheshang/CFD_GA_OPT/tree/master/data/opt.jpg)
