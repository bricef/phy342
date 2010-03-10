#Superposition theorem

Superposition theorem states that a network containing several voltage sources may be analysed by considering the effect of each source in turn. Simply by changing the voltage source with a resistor that has a value of internal resistance. 
The total current on the component is equal to algebraic sum of all currents obtained from different sources.

The simple example will be considered to represent this theory.

A circuit consists of two voltage sources (bateries) with internal resistance of 2 and 3 ohms respectively and a light bulb with a resistance of 50 ohms. Bateries supply 5 V each. What is the current that flows through the bulb ?

{@class=centre}
![Superposition](../resources/sup_1.jpg) 

Using Superposition Theorem, we will find the current produced by first baterry.
Replace the second batery with a resistor. The simplyfied circuit becomes:

{@class=centre}
![Superposition](../resources/sup_2.jpg) 

From the circuit above we can see that there is one resistor in series and another two in paralel.

Total resistance of the circuit is given by 

$$R_t=R_2+\frac{R_bR_3}{R_b+R_3}=4.83\gama$$

The current through bulb ($R_b$) can be found using potential divider 

$$V_b=\frac{V}{R_t} R_p$$ 

So $I_b=\frac{V_b}{R_b}$ 	and   $I_b=0.0586 A$ 

Now lets consider different batery. Performing same simplifications our circuit becomes:

{@class=centre}
![Superposition](../resources/sup_3.jpg) 

And the current passing through the bulb is $I_b=0.04 A$


Then according to superposition theory the total current that passes through light bulb is equal to 

$$I=I_1+I_2=0.098 A$$

If resistance and the current are known, the voltage across this bulb can be easily calculated using Ohm's Law.