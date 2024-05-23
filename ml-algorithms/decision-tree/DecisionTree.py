import numpy as np
from typing import Counter
def entropy(y):
    p_x= np.bincount(y)/len(y)
    return -np.sum([p*np.log(p) for p in p_x if p > 0])

class Node:
    def __init__(self, feature= None, threshold= None, left= None, right= None,* ,value= None):
        self.feature= feature
        self.threshold= threshold
        self.left= left
        self.right= right
        self.value= value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, min_samples_split= 2, max_depth= 100, n_features= None):
        self.min_samples_split= min_samples_split
        self.max_depth= max_depth
        self.n_features= n_features
        self.root= None

    def _most_common_label(self, y):
        return Counter(y).most_common(1)[0][0]

    def _information_gain(self, y, X_column, split_thres):
        parent= entropy(y)
        left_idxs, right_idxs= self._split(X_column, split_thres)
        if len(left_idxs)==0 or len(right_idxs)==0:
            return 0;
        n= len(y)
        n_l, n_r= len(left_idxs), len(right_idxs)
        e_l, e_r= entropy(y[left_idxs]), entropy(y[right_idxs])

        child_entropy= (n_l/n)*e_l + (n_r/n)*e_r

        information_gain= parent- child_entropy
        return information_gain

    def _split(self, X_column, split_thres):
        left_idxs= np.argwhere(X_column<=split_thres).flatten()
        right_idxs= np.argwhere(X_column>split_thres).flatten()

        return left_idxs, right_idxs

    def _best_criteria(self, X, y, feat_idxs):
        best_gain= -1
        split_idx, split_thres= None, None
        for feat_idx in feat_idxs:
            X_column= X[:, feat_idx]
            thresholds= np.unique(X_column)
            for thres in thresholds:
                gain= self._information_gain(y, X_column, thres)
                if gain> best_gain:
                    best_gain= gain
                    split_idx= feat_idx
                    split_thres= thres

        return split_idx, split_thres

    def _grow_tree(self, X, y, depth= 0):
        n_samples, n_feats= X.shape
        n_labels= len(np.unique(y))

        if (depth>self.max_depth or n_labels==1 or n_samples< self.min_samples_split):
            leaf_value= self._most_common_label(y)
            return Node(value= leaf_value)

        feat_idxs= np.random.choice(n_feats, self.n_features, replace= False)
        best_feat, best_thres= self._best_criteria(X, y, feat_idxs)

        left_idxs, right_idxs= self._split(X[:,best_feat], best_thres)

        left= self._grow_tree(X[left_idxs,:], y[left_idxs], depth+1)
        right= self._grow_tree(X[right_idxs,:], y[right_idxs], depth+1)

        return Node(best_feat, best_thres, left, right)

    def fit(self, X, y):
        self.n_features= X.shape[1] if not self.n_features else min(self.n_features, X.shape[1])
        self.root= self._grow_tree(X, y)

    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        if x[node.feature]<= node.threshold:
            return self._traverse_tree(x, node.left)
        return self._traverse_tree(x, node.right)


    def predict(self, X):
        return np.array([self._traverse_tree(x, self.root) for x in X])

