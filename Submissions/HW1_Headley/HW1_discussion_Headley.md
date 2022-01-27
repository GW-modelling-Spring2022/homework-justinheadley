# HW 1 The Challenge - Justin Headley
## 1. Show, based on the flux with depth, that the model is steady state.  Repeat this for a homogeneous and for a heterogeneous column.
    In the homogenous column, I have shown that the unit flux throughout the entire column is a constant 0.0075, which means an equal amount of mass is entering the column as leaving it, for a net change in mass of 0. This is steady-state. For the heterogeneous column, although K changes throughout the column, q is still a constant 0.0097, also showing steady-state conditions.  
   
  ## 2. Show that the steady state flux agrees with the direct calculation based on the harmonic mean average K.  Write the equation defining the direct calculation of the flux.
    For both columns, the steady-state flux iteratively calculated in column K is the same as the direct solution in cell C10. The direct solution is calculated with Darcy's law: q=K*(dH/dz).
  
    In this case, K is Keq, which is a harmonic mean K. For the homogeneous column, K is constant, but for the heterogeneous column, 
   
     Keq = (Total # of cells) / [(# Z1 Cells / Z1 K) +(Z2 Cells / Z2 K)] 

     Keq = 12 / [(6.5 / .005)+ (5.5 / .010)] = .00649


## 3. Show the steady state head profile for a column with approximately equal-thickness layers that have different K values.
    The heterogeneous column has approximately the top half of the column with a K value of 0.005 and the bottom half with a K value of 0.010. Although both total hydraulic head (H) and pressure head (psi) decrease with height throughout the column, flux (q) is constant. 

## 4. Use the head profile to explain WHY the equivalent hydraulic conductivity, Keq, is closer to the lower of the two K values.
    I've added a column that shows pressure head specifically, and also added pressure head values to the graph. The graph shows that the rate of change of pressure head increases greatly in the cells with the lower associated K values. This is because H = z + psi, and the rate of chane of z is constant (it's just a spatial dimenson). 

    The "traffic jam" in the column is the part with the lower K. This lower hydraulic conductivity causes a bottleneck that makes the Keq of the column more closely resemble the lower K than the higher K. 

    One important thing to note is that the "traffic jam" analogy does NOT mean that the water in the high-K part of the column is moving faster and then having to slow down. All the water in the column is still fluxing at the same rate, regardless of a particular cell's K. 