Key Equations:

The cost function:

<img width="382" height="96" alt="image" src="https://github.com/user-attachments/assets/3e8063a1-249f-4a3d-844d-d27a48267a01" />
 
where J is the cost, X is the data, y is the actual values, θ is the parameters, and m is the length of y. It is the calculation of the mean square error.

The gradient descent update rule: 

<img width="382" height="96" alt="image" src="https://github.com/user-attachments/assets/c2e831bb-a9da-4fb7-b381-9c122d2c6123" />

Here, α is the learning rate, which determines the size of our steps in the descent. X<sup>T</sup> is the transpose of the data. Note, that it should have been multiplied by 2, as we take the derivative of a the mean squared error, but we can ignore this 2 and just consider it as a part of the learning rate coefficient.

Sigmoid: 
<img width="187" height="51" alt="image" src="https://github.com/user-attachments/assets/34dbccfe-73cd-4568-a6eb-02e3da530454" />


