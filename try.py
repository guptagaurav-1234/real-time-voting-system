import seaborn as sns
import matplotlib.pyplot as plt

# Sample data (replace with your values)
data = [[1.00, 0.42, 0.29, -0.69, 0.88],
        [0.42, 1.00, 0.46, -0.15, 0.73],
        [0.29, 0.46, 1.00, -0.10, 0.20],
        [-0.69, -0.15, -0.10, 1.00, -0.69],
        [0.88, 0.73, 0.20, -0.69, 1.00]]

features = ["HbA1c", "Blood Pressure", "BMI", "Medication Adherence", "Readmission Risk"]

sns.heatmap(data, xticklabels=features, yticklabels=features, 
            annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Feature Correlations in Chronic Disease Management")
plt.show()