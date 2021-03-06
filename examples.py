# encoding: utf8

import sys
from pyshould import *
from pyshould.expect import *

def foo():
    raise TypeError('Foo')
    pass

bar = [0]
def change_bar():
    global bar
    bar.append(1)

#1 | should.not_eq(1)

foo | should.throw(NameError).Or(TypeError)
foo | should.throw((NameError, TypeError))
it(foo).throws(regex='[Ff]oo')

(lambda:foo()) | should.throw(TypeError)

with should.throw(TypeError):
    1 | should.be_int
    raise TypeError('foo')

with should.not_throw:
    s = 'foo'

with should.throw(KeyError).or_throw(TypeError):
    raise TypeError('foo')


#with should.not_change(bar):
#    ','.join(bar) | should.equal('0')

#with should.change(bar):
#    bar.append(1)
#    ','.join(bar) | should.equal('0,1')



#change_bar | should.not_change(bar)
#change_bar | should.not_change(lambda:bar)


assert 1 | should.be_int
assert False | should.be_int.And_equal(0)


'1' | should.be_a_string
[] | should.be_a_dict.or_an_array()
(1,) | should.be_a_tuple()
1 | should.be_an_int()

True | should.be_truthy.and_not_eq(2)

it(1).truthy.integer.eq(1)


1 | should_not.equal(2).or_equal(3)
#1 | should.not_equal(1).or_equal(3)

1 | should_either.equal(2).equal(3).equal(1)


1 | should.equal(2).Or_equal(1).But_greaterthan(0)

expect(1).to_equal(1)
expect(1, 3).to_be_less_than(5)
expect_it(1).to_be_less_than(3)
expect_all([3,1]).to_be_less_than(5)
expect_any(3,1).to_be_equal_to(1)
expect_none(3,1).to_be_equal_to(5)

1 | should.equal(1).lt(10).desc('not equal or less')

20 | should.equal(20).or_less_than(10)
1 | should.equal(2).or_less_than(10)

#'a' | should.equal('a')
#1 | should.be_lessthan(10)

it(1).should_be_less_than(10).equal(1)
any_of(10,3).should_be_less_than(10)
all_of(3,3).should_be_less_than(10)
none_of(11,13).should_be_less_than(10)

# Support quantifiers when using | notation
any_of([10, 3]) | should.be_less_than(5)
all_of(10, 3) | should.be_greater_than(1)
#none_of(10, 3) |


[3,1] | should_all.be_less_than(10)
[3,1] | should_any.be_less_than(2)
[3,1] | should_none.be_less_than(1)


#1 | should.check(lambda v: v < 2)
#any_of([1,3]).should_check(lambda v: v < 2)
#all_of(1, 3).should_check('v < 2')
#all_of(1, 3) | should.check(lambda v: v < 2)


1 | should_not.be_equal_to(2)



