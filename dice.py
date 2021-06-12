import random
import plotly.express as px

dice_result = []
dice_count = []

for i in range(0, 1000):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    dice_result.append(dice_sum)
    dice_count.append(i)

figure = px.bar(x = dice_result, y = dice_count)
figure.show()