import arithmetic;
from showLog import showError;
sum = arithmetic.add(1,2);
print("module.methpd:",sum)

ans = arithmetic.subtract(2,1);
print("module.methpd:",ans)

showError("Error 1")

from showLog import showData as pr;

pr("Hello this is alias import");

import learn as ln;

ln.learn("machine")

from learn import *
learn("From * :")