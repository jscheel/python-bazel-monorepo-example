load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "generated_lib",
    srcs = glob(["**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [
      requirement("protobuf"),
      requirement("grpcio"),
    ]
)
