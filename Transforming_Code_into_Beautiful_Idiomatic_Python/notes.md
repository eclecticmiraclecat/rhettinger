# Transforming Code into Beautiful, Idiomatic Python

Notes from Raymond Hettinger's talk at pycon US 2013 [video](http://www.youtube.com/watch?feature=player_embedded&v=OSGv2VnC0go), [slides](https://speakerdeck.com/pyconslides/transforming-code-into-beautiful-idiomatic-python-by-raymond-hettinger-1).

Modified [gist](https://gist.github.com/0x4D31/f0b633548d8e0cfb66ee3bea6a0deff9) for python3 and for own understanding

## Looping over a range of numbers
```py
for i in [0, 1, 2, 3, 4, 5]:
    print(i**2)

```

### Better

```py
for i in range(6):
    print(i**2)
```


## Looping over a collection

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(colors[i])
```

### Better

```python
for color in colors:
    print(color)
```

## Looping backwards

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)-1, -1, -1):
    print(colors[i])
```

### Better

```python
for color in reversed(colors):
    print(color)
```

## Looping over a collection and indices

```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(i, '--->', colors[i])
```

### Better

```python
for i, color in enumerate(colors):
    print(i, '--->', color)
```
> It's fast and beautiful and saves you from tracking the individual indices and incrementing them.

> Whenever you find yourself manipulating indices [in a collection], you're probably doing it wrong.

## Looping over two collections

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '--->', colors[i])

```

### Better

```python
for name, color in zip(names, colors):
    print(name, '--->', color)
```

## Looping in sorted order

```python
colors = ['red', 'green', 'blue', 'yellow']

# Forward sorted order
for color in sorted(colors):
    print(color)

# Backwards sorted order
for color in sorted(colors, reverse=True):
    print(color)
```

## Custom Sort Order

```python
colors = ['red', 'green', 'blue', 'yellow']

print(sorted(colors, key=len))
```

## Call a function until a sentinel value

```python
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)
```

### Better

```python
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
```

`iter` takes two arguments. The first you call over and over again and the second is a sentinel value.

## Distinguishing multiple exit points in loops

```python
def find(seq, target):
    found = False
    for i, value in enumerate(seq):
        if value == target:
            found = True
            break
    if not found:
        return -1
    return i
```

### Better

```python
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i
```

Inside of every `for` loop is an `else`.

## Looping over dictionary keys and values

```python
# Not very fast, has to re-hash every key and do a lookup
for k in d:
    print(k, '--->', d[k])
```

### Better

```python
for k, v in d.items():
    print(k, '--->', v)
```

## Construct a dictionary from pairs

```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))
# {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
```

## Counting with dictionaries

```python
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

# Simple, basic way to count. A good start for beginners.
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

# {'blue': 1, 'green': 2, 'red': 3}
```

### Better

```python
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1

from collections import defaultdict, Counter

d = defaultdict(int)
for color in colors:
    d[color] += 1

d = Counter(colors)
```

## Grouping with dictionaries -- Part I and II

```python
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

# In this example, we're grouping by name length
d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

# {5: ['roger', 'betty'], 6: ['rachel', 'judith'], 7: ['raymond', 'matthew', 'melissa', 'charlie']}

d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
```

### Better

```python
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
```

## Clarify function calls with keyword arguments

```python
twitter_search('@obama', False, 20, True)
```

### Better

```python
twitter_search('@obama', retweets=False, numtweets=20, popular=True)
```

Is slightly (microseconds) slower but is worth it for the code clarity and developer time savings.

## Clarify multiple return values with named tuples

```python
# Old testmod return value
doctest.testmod()
# (0, 4)
# Is this good or bad? You don't know because it's not clear.
```

### Better

```python
# New testmod return value, a namedTuple
doctest.testmod()
# TestResults(failed=0, attempted=4)
```

A namedTuple is a subclass of tuple so they still work like a regular tuple, but are more friendly.

To make a namedTuple:

```python
TestResults = namedTuple('TestResults', ['failed', 'attempted'])
```

## Unpacking sequences

```python
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

# A common approach / habit from other languages
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]
```

### Better

```python
fname, lname, age, email = p

Person = namedTuple('Person', ['fname', 'lname', 'age', 'email'])

p = Person('Raymond', 'Hettinger', 0x30, 'python@example.com')
```

The second approach uses tuple unpacking and is faster and more readable.

## Updating multiple state variables

```python
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t
```

### Better

```python
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x + y
```

Problems with first approach

 * x and y are state, and state should be updated all at once or in between lines that state is mis-matched and a common source of issues
 * ordering matters
 * it's too low level

The second approach is more high-level, doesn't risk getting the order wrong and is fast.

## Simultaneous state updates

```python
tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy
```

### Better

```python
x, y, dx, dy = (x + dx * t,
                y + dy * t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y'))
```

## Efficiency
 * An optimization fundamental rule
 * Don’t cause data to move around unnecessarily
 * It takes only a little care to avoid O(n**2) behavior instead of linear behavior

> Basically, just don't move data around unecessarily.

## Concatenating strings

```python
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
    s += ', ' + name
print(s)
```

### Better

```python
print(', '.join(names))
```

## Updating sequences

```python
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

del names[0]
# The below are signs you're using the wrong data structure
names.pop(0)
names.insert(0, 'mark')
```

### Better

```python
names = deque(['raymond', 'rachel', 'matthew', 'roger',
               'betty', 'melissa', 'judith', 'charlie'])

# More efficient with deque
del names[0]
names.popleft()
names.appendleft('mark')
```
## Decorators and Context Managers
 * Helps separate business logic from administrative logic
 * Clean, beautiful tools for factoring code and improving code reuse
 * Good naming is essential.
 * Remember the Spiderman rule: With great power, comes great responsibility!

## Using decorators to factor-out administrative logic

```python
# Mixes business / administrative logic and is not reusable
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page
```

### Better

```python
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
```

Note: since python 3.2 there is a decorator for this in the standard library: `functools.lru_cache`.

## Factor-out temporary contexts

```python
# Saving the old, restoring the new
old_context = getcontext().copy()
getcontext().prec = 50
print(Decimal(355) / Decimal(113))
setcontext(old_context)
```

### Better

```python
with localcontext(Context(prec=50)):
    print(Decimal(355) / Decimal(113))
```

## How to open and close files

```python
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()
```

### Better

```python
with open('data.txt') as f:
    data = f.read()
```

## How to use locks

```python
# Make a lock
lock = threading.Lock()

# Old-way to use a lock
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()
```

### Better

```python
# New-way to use a lock
with lock:
    print('Critical section 1')
    print('Critical section 2')
```

## Factor-out temporary contexts

```python
try:
    os.remove('somefile.tmp')
except OSError:
    pass
```

### Better

```python
with ignored(OSError):
    os.remove('somefile.tmp')
```

`ignored` is is new in python 3.4, [documentation](http://docs.python.org/dev/library/contextlib.html#contextlib.ignored).
Note: `ignored` is actually called `suppress` in the standard library.

To make your own `ignored` context manager in the meantime:

```python
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
```

> Stick that in your utils directory and you too can ignore exceptions

## Factor-out temporary contexts

```python
# Temporarily redirect standard out to a file and then return it to normal
with open('help.txt', 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstdout
```

### Better

```python
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
```

`redirect_stdout` is proposed for python 3.4, [bug report](http://bugs.python.org/issue15805).

To roll your own `redirect_stdout` context manager

```python
@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fieldobj
    finally:
        sys.stdout = oldstdout
```

## Concise Expressive One-Liners
Two conflicting rules:

 * Don’t put too much on one line
 * Don’t break atoms of thought into subatomic particles

Raymond’s rule:

 * One logical line of code equals one sentence in English

## List Comprehensions and Generator Expressions

```python
result = []
for i in range(10):
s = i ** 2
    result.append(s)
print(sum(result))
```

### Better

```python
print(sum(i**2 for i in xrange(10)))
```

First way tells you what to do, second way tells you what you want.
