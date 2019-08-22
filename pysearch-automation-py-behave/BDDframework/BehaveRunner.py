import glob
import sys
from behave import __main__ as runner_with_options

if __name__ == '__main__':
    sys.stdout.flush()
    # run Behave + BDD + Python code
    featureFilePath = ' features '
    commonRunnerOptions = ' --no-capture --no-capture-stderr -f plain '
    fullRunnerOptions = featureFilePath + commonRunnerOptions
    runner_with_options.main(fullRunnerOptions)
