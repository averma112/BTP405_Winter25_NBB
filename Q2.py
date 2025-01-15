import matplotlib.pyplot as plt
month = ["January", "February", "March", "April", "May", "June", "July",
         "August", "Septempber", "October", "November", "December"]
rainfall = [75, 60, 100, 125, 175, 200, 225, 210, 180, 140, 90, 80]



plt.figure(figsize=(10,6))
plt.bar(month, rainfall, color="red", edgecolor="black")

plt.xlabel("Months")
plt.ylabel("Rainfall")
plt.title("Monthly Rainfall Distribution", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
#Show the plot using plt.show
plt.show()
