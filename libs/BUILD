load("@pip_deps//:requirements.bzl", "requirement")


# py_library(
#     name = "proto",
#     srcs = glob(["**/*.py"]),
#     visibility = ["//visibility:public"],
#     deps = [
#       requirement("protobuf"),
#       requirement("grpcio")
#     ]
# )

# load("@rules_proto_grpc//python:defs.bzl", "python_grpc_library")
# load("@rules_proto_grpc//python:defs.bzl", "python_grpc_compile")
# python_grpc_compile(
#     name = "text_generation_proto_lib",
#     protos = ["//proto:rpc/ai/text_generation"],
# )
python_libary(
  name = "proto",
  srcs = [
    "//libs/proto:text_generation_proto_lib"
  ]
)
