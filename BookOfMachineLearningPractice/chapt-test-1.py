import matplotlib.pyplot as plt

x=[[6],[8],[10],[14],[18]];
y=[[7],[9],[13],[17.5],[18]];

plt.figure();
plt.title("Pizza diameter vs pizza price");
plt.xlabel("Pizza Diameter");
plt.ylabel("Pizza Price");

plt.axis([0,25,0,25]);
plt.plot(x,y,'k.');
plt.show();