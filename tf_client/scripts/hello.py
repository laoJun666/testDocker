#!/usr/bin/python
import argparse
import sys

import tensorflow as tf
import helper

FLAGS = None




#
# def main(unused_args):
#   # Create Protobuf ServerDef
#   # server_def = tensorflow_server_pb2.ServerDef(protocol="grpc")
#
#   # Cluster info
#   parse_cluster_spec(FLAGS.cluster_spec, server_def.cluster, FLAGS.verbose)
#
#   # Job name
#   if not FLAGS.job_name:
#     raise ValueError("Empty job_name")
#   server_def.job_name = FLAGS.job_name
#
#   # Task index
#   if FLAGS.task_id < 0:
#     raise ValueError("Invalid task_id: %d" % FLAGS.task_id)
#   server_def.task_index = FLAGS.task_id
#
#   config = config_pb2.ConfigProto(gpu_options=config_pb2.GPUOptions(
#       per_process_gpu_memory_fraction=FLAGS.gpu_memory_fraction))
#
#   # Create GRPC Server instance
#   server = server_lib.Server(server_def, config=config)
#
#   # join() is blocking, unlike start()
#   server.join()

def main(_):

    print("cluster_spec",helper.tf_cluster.parse_cluster_spec(FLAGS.cluster_spec))
    # print("ps_hosts",FLAGS.ps_hosts)
    # print("work_hosts",FLAGS.worker_hosts)
    # print("job_name",FLAGS.job_name)
    print("Index",FLAGS.task_id)


    print("hello,world!!")


if __name__ == "__main__":

    parser = helper.tf_cluster.getDefaultArgparse()
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
 




