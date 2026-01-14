# recall is TP/(TP+FN). It tells how frequently we catch actual positives
# precision is TP/(TP+FP). It tells how often a positive prediction is correct
import numpy as np

patient_test_results = np.array([1, 0, 0, 1, 1, 0, 1, 0, 1, 0])
predicted_health_status = np.array([1, 0, 1, 1, 1, 0, 0, 1, 1, 0])

# TODO: Calculate and assign how many True Negatives we have.
# TODO: Calculate and assign how many False Positives we have.
TN = np.sum((predicted_health_status == 0) & (patient_test_results == 0))
FP = np.sum((predicted_health_status == 1) & (patient_test_results == 0))
FN = np.sum((predicted_health_status == 0) & (patient_test_results == 1))
TP = np.sum((predicted_health_status == 1) & (patient_test_results == 1))

print(f"Confusion Matrix:\nTP: {TP}, FP: {FP},\nFN: {FN}, TN: {TN}")