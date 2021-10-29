# seldom -install chrome
# seldom -install firefox

# main() method is seldom run test entry method, It provides some of the most basic and important configurations.
import seldom

# ...

if __name__ == '__main__':

    seldom.main(path="./",
                browser="chrome",
                base_url="",
                report=None,
                title="project name",
                description="Environment description",
                debug=False,
                rerun=0,
                save_last_run=False,
                timeout=None,
    )

# Run Test (Run under a terminal (recommended))

# Create the file run.py, And import main() method.

import seldom


seldom.main()
# main() Method Run the use case in the current file by default.

# python run.py      # Run with the Python command
# seldom -r run.py   # Run with the Seldom command

# Run a class or method
# The seldom -m command can provide a more granular run.

# seldom -m test_sample     #  test_sample.py file
# seldom -m test_sample.SampleTest      #  SampleTest Class
# seldom -m test_sample.SampleTest.test_case    # test_case method





