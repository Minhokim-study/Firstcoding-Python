'''
import mymodule
mymodule.say_hi()

print('Version', mymodule.__version__)
'''
'''
from mymodule import say_hi, __version__
say_hi()

print('Version', __version__)
'''
from mymodule import *  #이 때는 앞에 __가 붙은 변수는 사용할 수가 없다
say_hi()
