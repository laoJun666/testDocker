#!/usr/bin/python
# -*- coding: UTF-8 -*

import argparse

''''
提供一些参数解析服务
'''


def parse_cluster_spec(cluster_spec, verbose=False):
  """Parse content of cluster_spec string and inject info into cluster protobuf.
  Args:
    cluster_spec: cluster specification string, e.g.,
          "local|localhost:2222;localhost:2223"
          "worker|tf-worker0:2222;tf-worker1:2222,ps|tf-ps0:2222"
    verbose: If verbose logging is requested.
  Raises:
    ValueError: if the cluster_spec string is invalid.
  """

  job_strings = cluster_spec.split(",")

  if not cluster_spec:
    raise ValueError("Empty cluster_spec string")

  cluster_spec_dict = {}
  for job_string in job_strings:
    if job_string.count("|") != 1:
      raise ValueError("Not exactly one instance of '|' in cluster_spec")

    job_name = job_string.split("|")[0]

    if not job_name:
      raise ValueError("Empty job_name in cluster_spec")

    if verbose:
      print("Added job named \"%s\"" % job_name)

    job_tasks = job_string.split("|")[1].split(";")
    for i in range(len(job_tasks)):
      if not job_tasks[i]:
        raise ValueError("Empty task string at position %d" % i)
      if verbose:
        print("  Added task \"%s\" to job \"%s\"" % (job_tasks[i], job_name))

    cluster_spec_dict[job_name] = job_tasks

  if verbose :
      print(cluster_spec_dict)

  return cluster_spec_dict



def getDefaultArgparse():
    """
    获得默认的tf集群脚本启动参数解析对象
    :return: 默认tf集群脚本启动参数解析对象
    """
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
        "--cluster_spec",
        type=str,
        default="",
        help="""\
            Cluster spec: SPEC.     SPEC is <JOB>(,<JOB>)*,"     JOB  is
            <NAME>|<HOST:PORT>(;<HOST:PORT>)*,"     NAME is a valid job name
            ([a-z][0-9a-z]*),"     HOST is a hostname or IP address,"     PORT is a
            port number." E.g., local|localhost:2222;localhost:2223,
            ps|ps0:2222;ps1:2222\
            """
    )
    parser.add_argument(
        "--job_name",
        type=str,
        default="",
        help="Job name: e.g., local"
    )
    parser.add_argument(
        "--task_id",
        type=int,
        default=0,
        help="Task index, e.g., 0"
    )
    parser.add_argument(
        "--gpu_memory_fraction",
        type=float,
        default=1.0,
        help="Fraction of GPU memory allocated", )
    parser.add_argument(
        "--verbose",
        type="bool",
        nargs="?",
        const=True,
        default=False,
        help="Verbose mode"
    )

    return  parser