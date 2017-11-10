# jenkins-test-optimizer

The aim  of this project is to explore the boundaries of software test automation
in a continuous delivery pipeline by implementing a re-ordering algorithm
to optimally sort the test cases such that tests with a higher likely hood of failing
are executed first, thus enabling faster feedback for failed tests to developers.

**This is a WIP**
-----------------

To test it:

- Clone repository

  cd jenkins-test-optimizer

- TO generate testset: Run test_generator.py

  $ ./test_generator.py <no of tests>
  $ ./test_generator.py 200

- The geenrated tests are stored under 'datasets/' and name of the file containing generated tests:

  $ datasets/testdataset.csv

- To Re-order tests using algorithm script: Run test_reordering_algorithm.py

  $ ./test_reordering_algorithm.py datasets/testdataset.csv
