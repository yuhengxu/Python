#修改、添加和删除元素#

#%%
#修改确定位置元素的值
motorcycles = ['honda', 'yanaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#在列表中添加元素

#%%
##在列表结尾添加元素
motorcycles.append('honda')
print(motorcycles)

#%%
##创建动态数组
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#%%
##在列表中插入元素 使用方法insert可在列表的任何位置添加新元素
motorcycles.insert(0, 'ducati')
print(motorcycles)

##从列表中删除元素 
#%%
### del可删除任何位置的列表元素，条件是知道其索引
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#%%
###使用pop删除
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#%%
###使用pop弹出列表中任何位置的元素
motorcycles = ['honda', 'yanaha', 'suzuki']
second_owned = motorcycles.pop(1)
print('The second motocycle I owend was a ' + second_owned.title() + '.')

#%%
###使用方法remove根据值删除元素,如果要删除的值在列表中存在多个，只能删除第一个
motorcycles = ['honda', 'yanaha', 'suzuki']
motorcycles.remove('yanaha')
print(motorcycles)

