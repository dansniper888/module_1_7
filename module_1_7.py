immutable_var = 1, 2, 'aplle', 2, 'sample'
# immutable_var .remove(2)
# AttributeError: 'tuple' object has no attribute 'remove'
print(immutable_var)
mutable_list = ['badge', 'clip', 'compass', 'eraser']
mutable_list .extend(['holder'])
print(mutable_list)
