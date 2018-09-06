#!/bin/bash
./launched.py --cluster_spec="worker|tf-worker0:2222,ps|tf-ps0:2222;tf-ps1:2222" \
              --job_name=ps\
              --task_id=1
