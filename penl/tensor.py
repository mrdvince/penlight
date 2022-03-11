import torch


def tensor(arr, requires_grad=True):
    return torch.tensor(arr, requires_grad=requires_grad)


def matmul(weights, bias):
    return torch.matmul(weights, bias.T)


def eye(n, requires_grad=True):
    return torch.eye(n, requires_grad=requires_grad)
