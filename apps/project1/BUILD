load("@pip_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")

package(default_visibility = ["//visibility:public"])

py_binary(
  name = "app",
  srcs = glob(["**/*.py"]),
  main = 'cli.py',
  deps = [
    "//libs/lib1",
    requirement("humanize")
  ]
)

py3_image(
    name = "image",
    srcs = glob(["**/*.py"]),
    deps = [
      "//libs/lib1",
      requirement("humanize")
    ],
    main = "cli.py",
)
