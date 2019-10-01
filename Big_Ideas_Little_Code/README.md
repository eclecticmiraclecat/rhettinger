# Lesson1_building_foundational_python_skills_for_data_analytics

Resampling
===========

Big Idea:

> Statistics modeled in a program are easier to get right and understand than using a formulaic approach. It is also extends to more complicated situations that classic formulas.

Topics to Prepare for Resampling
============================

* F-strings
* Counter(), most_common, elements
* Statistics
* Random: seed gauss triangular expovariate choice choices sample shuffle
* Review list concatenation, slicing, count/index, sorted()
* Review lambda expressions and chained comparisons

# Lesson5_building_additional_skills_for_data_analysis
Cluster Analysis of Voting Blocks
============================

Big Idea:
> Analyze public records to identify congressional voting blocks

Preparations for Cluster Analysis of Voting Blocks
=========================================

* defaultdict for accumulating data (tabulating)
* defaultdict for reversing a one-to-many mapping
* glob
* reading files with an encoding
* using next() or islice() to remove elements from an iterator
* csv.reader
* tuple unpacking
* looping idioms: enumerate, zip, reversed, sorted, set
* incrementing instances of Counter
* assertions

Applications to Congressional Voting Dataset
======================================
* Accumulate voting record for each U.S Senator for the 114th Congress.
* Use k-means to identify clusters of like voters
* Display the clusters and their actual party affiliations

# Lesson7_gearing_up_for_pub_sub_application
Publisher/Subscriber Service
========================

Big Idea:
> Users make posts. Followers subscribe to the posts they are interested in. Newer posts are more relevant. Display posts by a user, posts for a user, or posts matching a search request. Display followers of a user. Display those followed by a user. Store the user account information with hashed passwords.

Tools We Will Need
=============

* Unicode normalizion. NFC: chr(111)+chr(776) -> chr(246)
* Named tuples
* sorted(), bisect() and merge() -- reverse and key arguments
* itertools.islice()
* sys.intern()
* random.expovariate()
* time.sleep() and time.time()
* hashlib: pbkdf2_hmac, sha256/512, digest, hexdigest
* repr of a tuple
* joining strings
* floor division
* ternary operator
* and/or short-circuit boolean operators that return a value

# Lesson8_implementing_a_pub_sub_application
Publisher/Subscriber Service
==================

Big Idea:
> Users make posts. Followers subscribe to the posts they are interested in. Newer posts are more relevant. Display posts by a user, posts for a user. Display those followed by a user. Store the user account information with hashed passwords.

# Lesson9_using_bottle_to_build_REST_apis_and_web_application
Web Application written in Bottle
================

Big Idea:
> Micro-webframeworks (such as Bottle) are all about minimizing the code and effort required to links an application to a web server. Decorators connect a router or path to a function. The function managers getting a user request, calling the application and forming the response.

Tools We Will Need
=============

* Empty server with run()
* Returning static content
* Content type
* Content negotiation and vary header
* Dynamic Content
* Dynamic path
* Queries
* Cache-control
* Templates

# Lesson11_testing_and_data_validators
Approaches to Testing and Error Prevention
==============

Big Ideas:
> Python is a dynamic language. That lests us use the power of Python itself for testing.

Tools and Examples
=========

Quadratic equation example
------------

* Pyflakes
    - Names which are used but not defined or used before they are defined
    - Names which redefined without having been used
* Doc test
* mypy
* py.test
* itertools combinatorics
* hypothesis

Pricing tool
---------

* Validators