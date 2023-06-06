# load("@pip_deps//:requirements.bzl", "requirement")
# load("@rules_proto_grpc//python:defs.bzl", "python_grpc_compile")

# proto_library(
#   name = "proto/rpc/ai/text_generation",
#   srcs = ["proto/rpc/ai/text_generation.proto"],
#   visibility = ["//visibility:public"],
# )

# NOTE (jscheel): We are not using python_grpc_library because it tries to
# compile grpcio and screws up royally because we are doing cross-compilation.
# Instead, we have to compile the grpc stubs and expose them via a py_libary
# target manually that specifies tje proper deps itself.
# This has to be done at the root because protoc uses the src file path to
# create the package naming. It's a stupid decision that has caused nothing but
# problems, but no-one at Google gives enough of a darn to fix it.
# python_grpc_compile(
#   name = "proto_generated_lib",
#   protos = ["proto/rpc/ai/text_generation"],
#   output_mode = "NO_PREFIX",
#   visibility = ["//visibility:public"]
# )

# py_library(
#     name = "proto_lib",
#     srcs = ["proto_generated_lib"],
#     imports = ["proto_generated_lib"],
#     visibility = ["//visibility:public"],
#     deps = [
#       # "@com_google_protobuf//:protobuf_python",
#       requirement("protobuf"),
#       requirement("grpcio"),
#     ]
# )
