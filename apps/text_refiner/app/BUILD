load("@pip_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")
load("@io_bazel_rules_docker//lang:image.bzl", "app_layer")
load("@io_bazel_rules_docker//container:container.bzl", "container_layer", "container_image")

package(default_visibility = ["//visibility:public"])

deps = [
  "//libs/ai",
  requirement("quart"),
  requirement("openai"),
  requirement("langchain"),
  requirement("python-dotenv"),
]

py_binary(
  name = "binary",
  srcs = glob(["**/*.py"]),
  main = 'server.py',
  deps=deps,
)

container_layer(
  name = "python_symlink",
  symlinks = {
    "/usr/bin/python": "/usr/local/bin/python",
    "/usr/bin/python3": "/usr/local/bin/python",
  },
)

container_image(
  name = "python",
  base = "@python_container//image",
  layers = [":python_symlink"],
  visibility = ["//visibility:public"],
)

py3_image(
    name = "image",
    base = "python",
    srcs = glob(["**/*.py"]),
    deps=deps,
    main = "server.py",
)
