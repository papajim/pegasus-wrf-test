#!/bin/bash

tar -xzf FORCING.tar.gz
tar -xzf wrf_db.tar.gz

mpirun -np 2 /example_case/NWM/wrf_hydro_NoahMP.exe

tar -czf wrf_hydro_out.tar.gz diag_hydro* 2011* *\.2011*
