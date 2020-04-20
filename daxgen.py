#!/usr/bin/env python

import sys
import os
import pwd
import time
from Pegasus.DAX3 import *
from datetime import datetime
from argparse import ArgumentParser

def generate_wrf_workflow():
    "Generate a workflow"
    ts = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    dax = ADAG("wrf-test-%s" % ts)
    dax.metadata("name", "WRF Test")

    wrf_job = Job("wrf_wrapper")
    wrf_job.uses("hydro.namelist", link=Link.INPUT)
    wrf_job.uses("namelist.hrldas", link=Link.INPUT)
    wrf_job.uses("wrf_db.tar.gz", link=Link.INPUT)
    wrf_job.uses("FORCING.tar.gz", link=Link.INPUT)
    #wrf_job.addArguments("-w", "2", "/example_case/NWM/wrf_hydro_NoahMP.exe")
    wrf_job.uses("wrf_hydro_out.tar.gz", link=Link.OUTPUT, transfer=True, register=False)
    dax.addJob(wrf_job)
        
    # Write the DAX file
    dax.writeXMLFile("wrf.dax")


if __name__ == '__main__':
    generate_wrf_workflow()
