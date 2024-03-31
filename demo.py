print("Let us make a reversed( ) function, but for slices.")
print("\nSuppose we tried the following function:")
x="def partReversedBadX2(p):p=reversed(p)";print(x);exec(x)
input("A problem here: overwriting instead of updating.")
x="L=list(range(12))# We'll try changing L:";print(x);exec(x)
x="partReversedBadX2(L[1:11]);print(L)";print(x);exec(x)
input("See that the contents of L did not change.")
input("So we try again. Let's make it update instead:")
x="def partReversedBad(p):p[:]=reversed(p)";print(x);exec(x)
x="partReversedBad(L[1:11]);print(L)";print(x);exec(x)
input("See that the contents of L still did not change.")
input("\nThis problem involves slices. It's OK if no slice:")
x="partReversedBad(L);print(L)";print(x);exec(x);print(x);exec(x)
input("\nQ:How can sliced data be updated? A:Use slice( ):")
x="def partReversed(p,s):p[s]=reversed(p[s])";print(x);exec(x)
x="partReversed(L,slice(1,11));print(L)";print(x);exec(x)
input("\nBTW, there's another way to do it for bytearrays:")
x="s='A quick brown fox jumps over the lazy dog.'";print(x);exec(x)
x="def f(x):x[10:15]=b'my cr'";print(x);exec(x)
x="ba=bytearray(s,'ascii');mv=memoryview(ba)";print(x);exec(x) 
x=r"f(ba[19:]);print(ba);f(mv[19:]);print(ba)";print(x);exec(x)