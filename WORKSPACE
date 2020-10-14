load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "com_google_logging",
    sha256 = "9e1b54eb2782f53cd8af107ecf08d2ab64b8d0dc2b7f5594472f3bd63ca85cdc",
    strip_prefix = "glog-0.4.0",
    urls = ["https://github.com/google/glog/archive/v0.4.0.zip"],
)

http_archive(
    name = "com_github_gflags_gflags",
    sha256 = "34af2f15cf7367513b352bdcd2493ab14ce43692d2dcd9dfc499492966c64dcf",
    strip_prefix = "gflags-2.2.2",
    urls = [
        "https://mirror.bazel.build/github.com/gflags/gflags/archive/v2.2.2.tar.gz",
        "https://github.com/gflags/gflags/archive/v2.2.2.tar.gz",
    ],
)

http_archive(
    name = "eigen",
    build_file = "//third_party/eigen",
    sha256 = "146a480b8ed1fb6ac7cd33fec9eb5e8f8f62c3683b3f850094d9d5c35a92419a",
    url = "https://gitlab.com/libeigen/eigen/-/archive/3.3.8/eigen-3.3.8.tar.gz",
    strip_prefix="eigen-eigen-c5e90d9e764e"
)