#`Th&eacute;venin's theorem

This is an extension of Superposition theory. Thevenin's theory is particulary very useful when we are looking at circuits where load resistance is changing. This saves us time to analyse the new circuit when resistance is changed.

An active network with terminals A and B can be replaced with a constant voltage source, V, with a magnitude that is equal to the open circuit voltage across terminals A and B.

To help to understand this theorem and show its usefulnes we will consider the folowing example:

We have a circuit that is shown below:

{@class=centre}
![Thevenin's Theorem](../resources/tev_1.jpg)

We will change this circuit leaving a constant voltage source, V, and a resistor connected in series to the voltage source.

{@class=centre}
![Thevenin's Theorem](../resources/tev_2.jpg)

If V and r are known we can see that any resistor connected to terminals A and B can be calculated very quickly. 

How to simplify such a circuit.

First of all we conssider an open circuit with no load connected to its terminals.

{@class=centre}
![Thevenin's Theorem](../resources/tev_3.jpg)

then we see that two resistors are connected in paralel so total resistance is:

$$\frac{1}{R_p}=\frac{1}{R_1}+\frac{1}{R_3}$$ or $$R_p=\frac{R_1R_3}{R_1+R_3}$$

So our circuit simplyfies to 

{@class=centre}
![Thevenin's Theorem](../resources/tev_4.jpg)

and again we can simplify our circuit even further

{@class=centre}
![Thevenin's Theorem](../resources/tev_5.jpg)

$$R_t=R_p+R_2$$
