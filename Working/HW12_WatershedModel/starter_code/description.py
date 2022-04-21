# The Big Challenge

## Model Description 
This is a steady state, layered box model with recharge, pumping, ET, and a stream with 3 segments. 

#### Dimensions: 
- 50 by 50 by 3
- dx = dy = 1000 m
- dz = 100 m  

#### Topography
- The bottom of the domain is topographically flat and the bottom layer is 40 m thick. The middle layer is 5 m thick and is also flat. The top layer elevation is provided in BASE_TOP_ELEV.CSV.

#### Subsurface Properties: 
- Homogeneous 
- Top & Bottom Layer K = 8.5 m/day in x, y, and z  
- K of the middle layer is the same as the lower layer in the leftmost 20 columns, but it is 0.0001 m/day in the z direction in the remaining columns.
- Porosity = 0.10
- Specific yield = 0.10
- Storage coefficient=0.0001  

#### Boundary Conditions: 
 
 - Right boundary is a constant head of 70m 
 - All other boundaries are no-flow
 - Recharge occurs at a rate of 4E-5 m/d in leftmost 15 columns and zero elsewhere. 
 
#### And more (see The_Challenge.md) 
