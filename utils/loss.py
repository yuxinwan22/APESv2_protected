import torch


def consistency_loss(tgt):
    """
    :param tgt: should be a list of tensors in shape BxNxD
    """
    loss = torch.nn.MSELoss()
    loss_list = []
    for i in range(len(tgt)):
        for j in range(len(tgt)):
            if i < j:
                loss_list.append(loss(tgt[i], tgt[j]))
            else:
                continue
    return sum(loss_list) / len(tgt)

def aux_loss(preds, cls_labels, loss_fn):
    """_summary_

    Args:
        preds (list): B*40
        cls_labels (_type_): B*40
        loss_fn (function): loss function
    """
    aux_loss = 0
    for i, pred in enumerate(preds):
        if i != len(preds)-1:
           aux_loss += loss_fn(pred, cls_labels)
    aux_loss = aux_loss / (len(preds) - 1)
    return aux_loss