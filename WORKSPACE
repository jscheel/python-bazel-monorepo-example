workspace(name = "python-bazel")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")
load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

http_archive(
    name = "bazel_skylib",
    sha256 = "b8a1527901774180afc798aeb28c4634bdccf19c4d98e7bdd1ce79d1fe9aaad7",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/1.4.1/bazel-skylib-1.4.1.tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/1.4.1/bazel-skylib-1.4.1.tar.gz",
    ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()


http_archive(
    name = "rules_python",
    sha256 = "94750828b18044533e98a129003b6a68001204038dc4749f40b195b24c38f49f",
    strip_prefix = "rules_python-0.21.0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.21.0/rules_python-0.21.0.tar.gz",
)




http_archive(
    name = "rules_pkg",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_pkg/releases/download/0.9.1/rules_pkg-0.9.1.tar.gz",
        "https://github.com/bazelbuild/rules_pkg/releases/download/0.9.1/rules_pkg-0.9.1.tar.gz",
    ],
    sha256 = "8f9ee2dc10c1ae514ee599a8b42ed99fa262b757058f65ad3c384289ff70c4b8",
)
load("@rules_pkg//:deps.bzl", "rules_pkg_dependencies")
rules_pkg_dependencies()



# k8s ==========================================================================
http_archive(
    name = "io_bazel_rules_k8s",
    sha256 = "ce5b9bc0926681e2e7f2147b49096f143e6cbc783e71bc1d4f36ca76b00e6f4a",
    strip_prefix = "rules_k8s-0.7",
    urls = ["https://github.com/bazelbuild/rules_k8s/archive/refs/tags/v0.7.tar.gz"],
)

load("@io_bazel_rules_k8s//k8s:k8s.bzl", "k8s_repositories")
k8s_repositories()
load("@io_bazel_rules_k8s//k8s:k8s_go_deps.bzl", k8s_go_deps = "deps")
k8s_go_deps()
# ==============================================================================





# kustomize ====================================================================
http_archive(
    name = "com_benchsci_rules_kustomize",
    sha256 = "7c2308991352d534c4ad3d9a0e37eee402ccb8a7c96eeb718c18c52f81c45fb1",
    strip_prefix = "rules_kustomize-4b979472aae1953799a616e45a10748acafcd982",
    urls = ["https://github.com/benchsci/rules_kustomize/archive/4b979472aae1953799a616e45a10748acafcd982.zip"],
)
load("@com_benchsci_rules_kustomize//:workspace.bzl", "download_kustomize_deps")
download_kustomize_deps()
# ==============================================================================









# docker =======================================================================
http_archive(
    name = "io_bazel_rules_docker",
    sha256 = "b1e80761a8a8243d03ebca8845e9cc1ba6c82ce7c5179ce2b295cd36f7e394bf",
    urls = ["https://github.com/bazelbuild/rules_docker/releases/download/v0.25.0/rules_docker-v0.25.0.tar.gz"],
)
load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)
container_repositories()

load("@io_bazel_rules_docker//repositories:deps.bzl", container_deps = "deps")

container_deps()

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
)

container_pull(
  name = "java_base",
  registry = "gcr.io",
  repository = "distroless/java",
  # 'tag' is also supported, but digest is encouraged for reproducibility.
  digest = "sha256:deadbeef",
)

# container_pull(
#   name = "python3-debian11",
#   registry = "gcr.io",
#   repository = "distroless/python3-debian11",
#   tag = 'latest',
# )

container_pull(
  name = "python_container",
  registry = "docker.io/library",
  repository = "python",
  tag = "3.10.8-slim",
)

container_pull(
  name = "python_container_debian",
  registry = "gcr.io",
  repository = "distroless/python3-debian11",
  tag = "latest",
)

load(
    "@io_bazel_rules_docker//repositories:repositories.bzl",
    container_repositories = "repositories",
)

container_repositories()

load(
    "@io_bazel_rules_docker//python3:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()
# ==============================================================================





# helm =========================================================================
git_repository(
    name = "com_github_masmovil_bazel_rules",
    commit = "5d23e9e2f8eb350d6fb179e811067351f6574233",
    # tag = "v0.5.0",
    remote = "https://github.com/masmovil/bazel-rules.git",
)
load(
    "@com_github_masmovil_bazel_rules//repositories:repositories.bzl",
    mm_repositories = "repositories",
)
mm_repositories()
# ==============================================================================






load("@rules_python//python/pip_install:repositories.bzl", "pip_install_dependencies")
pip_install_dependencies()


load("@rules_python//python:repositories.bzl", "py_repositories", "python_register_toolchains")
py_repositories()




# load("@rules_python//python:repositories.bzl", "python_register_toolchains")
python_register_toolchains(
    name = "python3_10_8",
    # Available versions are listed in @rules_python//python:versions.bzl.
    # We recommend using the same version your team is already standardized on.
    python_version = "3.10.8",
)

load("@python3_10_8//:defs.bzl", "interpreter")


load("@rules_python//python:pip.bzl", "pip_parse")
pip_parse(
    name = "pip_deps",
    requirements_lock = "//third-party:requirements_lock.txt",
    python_interpreter_target = interpreter,
    download_only = True,
    extra_pip_args = ["--platform", "manylinux2014_x86_64"],
    #extra_pip_args = ["--platform", "manylinux_2_17_x86_64"],
)


load("@pip_deps//:requirements.bzl", "install_deps")
install_deps()



# protobuf =====================================================================
http_archive(
    name = "rules_proto",
    sha256 = "dc3fb206a2cb3441b485eb1e423165b231235a1ea9b031b4433cf7bc1fa460dd",
    strip_prefix = "rules_proto-5.3.0-21.7",
    urls = [
        "https://github.com/bazelbuild/rules_proto/archive/refs/tags/5.3.0-21.7.tar.gz",
    ],
)
# load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
# rules_proto_dependencies()
# rules_proto_toolchains()





# https://github.com/rules-proto-grpc/rules_proto_grpc


# http_archive(
#     name = "com_github_grpc_grpc",
#     patch_args = ["-p1"],
#     patches = ["//tools/patches:grpc_extra_deps.patch"],
#     sha256 = "ec125d7fdb77ecc25b01050a0d5d32616594834d3fe163b016768e2ae42a2df6",
#     strip_prefix = "grpc-1.52.1",
#     urls = [
#         "https://github.com/grpc/grpc/archive/v1.52.1.tar.gz",
#     ],
# )

# http_archive(
#     name = "rules_proto_grpc",
#     sha256 = "928e4205f701b7798ce32f3d2171c1918b363e9a600390a25c876f075f1efc0a",
#     strip_prefix = "rules_proto_grpc-4.4.0",
#     urls = ["https://github.com/rules-proto-grpc/rules_proto_grpc/releases/download/4.4.0/rules_proto_grpc-4.4.0.tar.gz"],
# )
# load("@rules_proto_grpc//:repositories.bzl", "rules_proto_grpc_toolchains", "rules_proto_grpc_repos")
# rules_proto_grpc_toolchains()
# rules_proto_grpc_repos()

# load("@rules_proto//proto:repositories.bzl", "rules_proto_dependencies", "rules_proto_toolchains")
# rules_proto_dependencies()
# rules_proto_toolchains()

# load("@rules_proto_grpc//python:repositories.bzl", rules_proto_grpc_python_repos = "python_repos")
# rules_proto_grpc_python_repos()

# load("@com_github_grpc_grpc//bazel:grpc_deps.bzl", "grpc_deps")
# grpc_deps()

# load("@com_github_grpc_grpc//bazel:grpc_extra_deps.bzl", "grpc_extra_deps")
# grpc_extra_deps()


# ==============================================================================
