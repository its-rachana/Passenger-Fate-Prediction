# Calculate percentages
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../dataset/cleaned_dataset.csv")
cryo_transport = pd.crosstab(df['CryoSleep'], df['Transported'], normalize='index') * 100

not_transported_ids = df.loc[df['Transported'] == False, 'PassengerId']
print(not_transported_ids)
# Plot
# plt.figure(figsize=(10, 6))
# cryo_transport.plot(kind='bar', stacked=True, color=['#ff6b6b', '#74b9ff'])
# plt.title('Transportation Rate by CryoSleep Status (%)')
# plt.xlabel('In CryoSleep')
# plt.ylabel('Percentage')
# plt.legend(['Not Transported', 'Transported'], title='Outcome')
# plt.xticks([0, 1], ['No', 'Yes'], rotation=0)
# plt.show()
#
# vip_transport = pd.crosstab(df['VIP'], df['Transported'], normalize='index') * 100
#
# # Plot
# plt.figure(figsize=(10, 6))
# cryo_transport.plot(kind='bar', stacked=True, color=['#ff6b6b', '#74b9ff'])
# plt.title('Transportation Rate if VIP')
# plt.xlabel('Is VIP')
# plt.ylabel('Percentage')
# plt.legend(['Not Transported', 'Transported'], title='Outcome')
# plt.xticks([0, 1], ['No', 'Yes'], rotation=0)
# plt.show()