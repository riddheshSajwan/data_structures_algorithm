""" Google Question
Given an array = [2,5,1,2,3,5,1,2,4]:
It should return 2

Given an array = [2,1,1,2,3,5,1,2,4]:
It should return 1

Given an array = [2,3,4,5]:
It should return None

Bonus... What if we had this:// [2,5,5,2,3,5,1,2,4]
 return 5 because the pairs are before 2,2 """


def firstRecurringCharacter(nums):
    itemsLooped = []
    for item in nums:
        if item in itemsLooped:
            return item
        elif item != nums[-1]:
            itemsLooped.append(item)
    return None

print(firstRecurringCharacter([2,5,5,2,3,5,1,2,4])) #O(n^2) Space = O(1)

#Using Map
def firstRecurringCharacter2(nums):
    itemsLooped={}
    for item in nums:
        if itemsLooped.get(item):
            return item
        elif item != nums[-1]:
            itemsLooped.update({item:True})
    return None
print(firstRecurringCharacter2([2,5,5,2,3,5,1,2,4])) #O(n) Space = O(n)