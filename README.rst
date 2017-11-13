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

- The generated tests are stored under 'datasets/' and name of the file containing generated tests:

  $ datasets/testdataset.csv


- To generate multi user datasets from single testdata set use the multiuser_datasets.py:

  $ ./multiuser_datasets.py <testdataset file><no of users>
  
  $ ./multiuser_datasets.py datasets/testdataset_010242.csv 7

- To Re-order test sets using algorithm script: Run test_reordering_algorithm.py


  $ ./test_reordering_algorithm.py datasets/testdataset.csv

- To Re-order multiple testsets use script reorder_multiplesets.sh


  $ ./reorder_multiplesets.sh 
  
  $ # this script works now, but is a WIP


- To compute a sample impact value single pair


  $ ./computations.py <unsorted dataset> <sorted dataset>
  
  $ ./computations.py datasets/testdataset_010242.csv datasets/testdataset_010242.csv_sorted.csv


- For multiple sets: WIP

  $ ./computations_multiplesets.sh <directory name>
