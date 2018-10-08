import matplotlib.pyplot as plt

weight_list = [x for x in range(50, 120)]
def BMI(weight):
    result = weight/1.84
    return result/1.84
BMI_list = [round((x/1.84)/1.84, 2) for x in weight_list]
plt.plot(weight_list, BMI_list)
# plt.legend(x='weight', y='BMI')
plt.show()
