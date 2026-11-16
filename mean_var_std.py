import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError('List must contain nine numbers.')
    m = np.array(lst).reshape(3, 3)
    return {
        'mean': [m.mean(axis=0).tolist(), m.mean(axis=1).tolist(), float(m.mean())],
        'variance': [m.var(axis=0).tolist(), m.var(axis=1).tolist(), float(m.var())],
        'standard deviation': [m.std(axis=0).tolist(), m.std(axis=1).tolist(), float(m.std())],
        'max': [m.max(axis=0).tolist(), m.max(axis=1).tolist(), int(m.max())],
        'min': [m.min(axis=0).tolist(), m.min(axis=1).tolist(), int(m.min())],
        'sum': [m.sum(axis=0).tolist(), m.sum(axis=1).tolist(), int(m.sum())],
    }

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(calculate([2, 6, 2, 8, 4, 0, 1, 5, 7]))
try:
    calculate([1, 2, 3])
except ValueError as e:
    print('ValueError OK:', e)
