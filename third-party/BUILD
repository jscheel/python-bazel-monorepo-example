load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "//third-party:requirements.txt",
    requirements_txt = "//third-party:requirements_lock.txt",
    visibility = ["//visibility:public"],
    target_compatible_with = [
      # "@platforms//manylinux_2_24:x86_64"
      "@platforms//os:linux",
      "@platforms//cpu:x86_64"
    ],
)

# Repeat for each supported target platform
config_setting(
    name = "manylinux2014_x86_64",
    constraint_values = [
        "@platforms//os:linux",
        "@platforms//cpu:x86_64",
    ],
)

alias(
    name = "grpcio",
    actual = select({
        # Repeat for each target platform
        ":manylinux2014_x86_64": "@pip_manylinux2014_grpcio//:pkg",
        # ":manylinux1_x86_64": "@pip_deps_grpcio//:pkg"
        # ...
    }),
    visibility = ["//visibility:public"],
)
