# Installation and Usage

# pip install allure-behave

# behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features
# allure serve %allure_result_folder%

# Support behave parallel

# Current implementation of behave-parallel makes some allure features inaccessible.
# So in this case you need patch your environment.py files instead using formatter. If you don't use environment.py, just crate empty one with calling allure like in example below.

from allure_behave.hooks import allure_report


### your code

allure_report("path/to/result/dir")

