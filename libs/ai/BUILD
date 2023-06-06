load("@pip_deps//:requirements.bzl", "requirement")

py_library(
    name = "ai",
    srcs = glob(["**/*.py"]),
    visibility = ["//visibility:public"],
    deps = [
      requirement("redis"),
      requirement("openai"),
      requirement("langchain"),
      requirement("tiktoken"),
      requirement("pydantic"),
    ]
)
