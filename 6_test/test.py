from module1 import foo   # 从module1模块中导出foo函数
foo()
from module2 import foo
foo()


import module1 as m1
import module2 as m2
m1.foo()
m2.foo()

# 需要注意的是：如果导入的模块除了定义函数之外还有可以执行代码，那么python解释器在导入这个模块时就会执行这些代码，事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些代码放入这个如下所示的条件中，这样的话除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"

import module3
# 导入module3时，不会执行模块中if条件成立时的代码，因为模块的名字是module3而不是__main__