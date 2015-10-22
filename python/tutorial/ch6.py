"""
fibo.py 파일을 만들고, 그 파일을 다른 파일에서 import 할 수 있다.
"""
import fibo

fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

fib = fibo.fib
fib(500)

"""
기본적으로 내장되어 있는 모듈
sys.ps1 진행 시 python prompt가 >>> 에서 C> 로 바뀐다.
"""
import sys
sys.ps1

sys.ps2

sys.ps1 = 'C> '

"""
sys.path.append는 interpreter의 검색 경로를 결정하는데 사용
"""
sys.path.append('/ufs/guido/lib/python')


"""
dir 함수는 argument에 있는 값의 모듈을 불러오는데 사용
"""
dir(fibo)
dir(sys)


"""
argument없이 dir 함수를 호출시, 
현재 정의한 것을 가져온다.
아래 예제에서는 dir(fibo) 한 것과 동일한 내용
"""
a = [1, 2, 3, 4, 5]
fib = fibo.fib
dir()

import builtins
dir(builtins)


"""
6.4 Packages

from package import * 을 수행하면
예상대로라면 모든 모듈을 다 가져와야 되는데, 현실은 그렇지 않음

__init__.py에 __all__ = ["one", "two", "fibo" "..."]
이렇게 추가해주고

from package import *을 수행하면
원하는 모듈들이 모두 import 되어 있음


package를 import 할 때 상대 경로를 쓸 수 있음
ex) from . import echo
from ..filters import equalizer

package는 __path__ attribute를 지원함.
이것을 이용하면 search path에 영향을 줌
"""
