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


