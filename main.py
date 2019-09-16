import numpy as np
from utils import *
from analyze import *

def main():
    """
    main executable
    check times, put into intervals
    """

    # load parsed data
    data, driver_hash = getData()

    # analyze data
    analyze(data, driver_hash)

if __name__ == "__main__":
    main()