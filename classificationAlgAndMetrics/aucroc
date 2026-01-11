from matplotlib import pyplot as plt
from numpy import random

random.seed(42)

truth_labels = [1 if random.rand() > 0.6 else 0 for _ in range(100)]
predicted_probs = [max(0, min(1, random.normal(loc=label, scale=0.3))) for label in truth_labels]

def roc_curve(truth_labels, predicted_probs):
    thresholds = [0.1 * i for i in range(11)]
    tprs, fprs = [], []
    for threshold in thresholds:
        tp = fp = tn = fn = 0
        # TODO: calculate TP, FP, TN, FN
        for i in range(len(truth_labels)):
            if predicted_probs[i] >= threshold:
                if truth_labels[i] == 1:
                    tp += 1
                else:
                    fp += 1
            else:
                if truth_labels[i] == 1:
                    fn += 1
                else:
                    tn += 1
        # TODO: append a new TPR value to the tprs array
        tprs.append(tp/(tp+fn))
        # TODO: append a new FPR value to the fprs array
        fprs.append(fp/(tn+fp))
    return tprs, fprs

def compute_aucroc(tprs, fprs):
    aucroc = 0
    for i in range(1, len(tprs)):
        aucroc += 0.5 * abs(fprs[i] - fprs[i - 1]) * (tprs[i] + tprs[i - 1])
    return aucroc

tprs, fprs = roc_curve(truth_labels, predicted_probs)

plt.plot(fprs, tprs, marker='.')
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.show()

aucroc = compute_aucroc(tprs, fprs)
print(f"The AUC-ROC value is: {aucroc}")
