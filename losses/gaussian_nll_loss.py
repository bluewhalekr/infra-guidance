# Copyright (c) 2023, Zikang Zhou. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import torch
import torch.nn as nn
import torch.nn.functional as F


class GaussianNLLLoss(nn.Module):

    def __init__(self,
                 full: bool = False,
                 eps: float = 1e-2,  # 더 큰 값으로 조정
                 reduction: str = 'mean') -> None:
        super(GaussianNLLLoss, self).__init__()
        self.full = full
        self.eps = eps
        self.reduction = reduction

    def forward(self,
                pred: torch.Tensor,
                target: torch.Tensor) -> torch.Tensor:
        mean, var = pred.chunk(2, dim=-1)
        var = var.clone()
        with torch.no_grad():
            var.clamp_(min=self.eps)
        
        # 커스텀 Gaussian NLL with penalty
        nll = 0.5 * torch.log(2 * torch.pi * var) + 0.5 * (target - mean)**2 / var
        penalty = 0.1 * (1/var).mean()  # 분산이 작아지는 것을 방지
        
        if self.reduction == 'mean':
            return nll.mean() + penalty
        elif self.reduction == 'sum':
            return nll.sum() + penalty
        elif self.reduction == 'none':
            return nll + penalty
        else:
            raise ValueError('{} is not a valid value for reduction'.format(self.reduction))
