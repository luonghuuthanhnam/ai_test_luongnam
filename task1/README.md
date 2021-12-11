# Main idea:
## Preprocess data
 - Convert data to dictionary structor, relace curent key `LabelName` by the `value` of `LabelName`, it mean `key` is the labelname of each class, and `value` is `subcategories` of the `key` class.
Beacuse of call dict to retrieve data is the fastest way, algorithm complexity is O(1).<br />
 - Flatent Hierary Tree: Transform the Hierarchy Tree become a 1 level dictionary. This flatten dictionary include 601 pairs `key-value` (there are 601 categories in the hierarchy). 
Each `Pair` is a pair of `Child - [Parents]`
 - By that way, I can get parent of every class directly.<br />
## Some child have many parents
There are some child have many parent, so the Siblings of it is a combination of all chilren of it's parents.<br />

# Time consuming:
There are 2 steps:
 - Preprocessing data: `~0.04s` this step take longest time. But is is trade-of a faster runing time when lookup data. It doesn't matter as long as the `Category` stable in less changing than the frequence of lookup time. <br />
 - Look up time: `Fast`
  -- Parents: `~9e-6s`
  -- Siblings: `~0.0002s`
  -- Ancestors: `2e-5`
  -- Check Same Ancestors: `2.5e-5`
<img src="/task1/images/time_consuming.png">
<img src="/task1/images/time_consuming2.png">

# Feel Free to test it yourself
