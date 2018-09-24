"""
==========================================
One-class SVM with non-linear kernel (RBF)
==========================================

An example using a one-class SVM for novelty detection.

:ref:`One-class SVM <svm_outlier_detection>` is an unsupervised
algorithm that learns a decision function for novelty detection:
classifying new data as similar or different to the training set.
"""
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
from sklearn import svm


def oneclass_svm():
    X_train, X_test = np.random.normal(0, 1, (10000, 2)), np.random.normal(0, 1, (10000, 2))
    # Generate some abnormal novel observations
    X_outliers = np.random.normal(2.5, 0.3, (1000, 2))
    # fit the model
    clf = svm.OneClassSVM(nu=0.01, kernel="rbf", gamma=0.1)
    clf.fit(X_train)
    y_pred_train = clf.predict(X_train)
    y_pred_test = clf.predict(X_test)
    y_pred_outliers = clf.predict(X_outliers)
    n_error_train = y_pred_train[y_pred_train == -1].size
    n_error_test = y_pred_test[y_pred_test == -1].size
    n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size

    print(f'n_error_train = {n_error_train}\n'
          f'n_error_test = {n_error_test}\n'
          f'n_error_outliers = {n_error_outliers}')


if __name__ == '__main__':
    oneclass_svm()
