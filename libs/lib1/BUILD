load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "lib1",
    srcs = glob(["**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [
      requirement("piglatin")
    ]
)
