import matplotlib.pyplot as plt
import numpy as np

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x, y, color="blue", linewidth="4")
# plt.plot(x, y, "o--g")
# plt.axis([0, 6, 0, 20])

# plt.title("Grafik Başlığı")
# plt.xlabel("X Ekseni")
# plt.ylabel("Y Ekseni")

"""
x = np.linspace(0, 2, 100)

plt.plot(x, x, label="dogrusal")
plt.plot(x, x**2, label="karesel")
plt.plot(x, x**3, label="kupsel")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.legend()

plt.show()
"""
"""
x = np.linspace(0, 2, 100)
fgr, axs = plt.subplots(3)

axs[0].plot(x, x, color="red")
axs[0].set_title("dogrusal")

axs[1].plot(x, x**2, color="green")
axs[1].set_title("karesel")

axs[2].plot(x, x**3, color="blue")
axs[2].set_title("kupsel")

plt.tight_layout()

plt.show()
"""
# x = np.linspace(0, 2, 100)
# fgr, axs = plt.subplots(2, 2)
# fgr.suptitle("grafik basligi")

# axs[0, 0].plot(x, x, color="red")
# axs[0, 1].plot(x, x**2, color="green")
# axs[1, 0].plot(x, x**3, color="blue")
# axs[1, 1].plot(x, x**4, color="yellow")

# plt.show()

#######
import pandas as pd

# df = pd.read_csv("veri_setleri/DEvideos.csv")
# df = df.drop(["video_id"], axis=1).groupby("category_id").mean()
# df.head().plot(subplots=True)
# plt.legend()
# plt.show()
#######

x = np.linspace(-10, 9, 20)
y = x ** 3
z = x ** 2
"""
figur = plt.figure()
eksen_kup = figur.add_axes([0.1, 0.1, 0.8, 0.8])

eksen_kup.plot(x, y, "b")
eksen_kup.set_xlabel("X ekseni")
eksen_kup.set_ylabel("Y ekseni")
eksen_kup.set_title("Küp")

eksen_kare = figur.add_axes([0.15, 0.6, 0.25, 0.25])

eksen_kare.plot(x, z, "g")
eksen_kare.set_xlabel("X ekseni")
eksen_kare.set_ylabel("Y ekseni")
eksen_kare.set_title("Kare")

"""
"""
figur = plt.figure()
eksen = figur.add_axes([0, 0, 1, 1])

eksen.plot(x, z, label="Kare")
eksen.plot(x, y, label="Küp")
eksen.legend(loc=4)
plt.show()
"""
fgr, axes = plt.subplots(nrows=2, ncols=1, figsize=(4, 4))

eksen[0].plot(x, y)
eksen[0].set_title("Küp")
eksen[1].plot(x, z)
eksen[1].set_title("Kare")

plt.tight_layout()
# fig.savefig("figur1.pdf")

plt.show()