#!/usr/bin/python3
# -*- coding: UTF-8 -*-
num = float(input('Input:'))
num_sqrt = num ** 0.5
num_mod = num_sqrt % 2
if num_mod == 1.0 :
  steps = num_sqrt - 1
else:
  num_sqrt = int(num_sqrt)
  if int(num_mod) % 2 :
      num_sqrt_parity = num_sqrt
  else:
      num_sqrt_parity = num_sqrt - 1
  num_outer_site = num - (num_sqrt_parity * num_sqrt_parity)
  outer_long = num_outer_site - (num_outer_site // (num_sqrt_parity + 1)) * (num_sqrt_parity + 1)
  outer_steps = abs(outer_long - (num_sqrt_parity + 2) // 2)
  inner_stpes = (num_sqrt_parity + 2) // 2
  steps = outer_steps + inner_stpes
print('Answer:',int(steps))

