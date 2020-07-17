__version__ = "1.0.0"
import sys
from ksapriori.scan_dataset import scan_dataset
from ksapriori.load_data import load_dataset
from ksapriori.apriori import ksapriori
from ksapriori.generate_candidate import create_c1,create_ck
from ksapriori.association_rule import generate_rule

if (sys.version_info[0] < 3) or (sys.version_info[1] < 7):
    msg = "The `ksapriori` package only works for Python 3.7+."
    raise Exception(msg)