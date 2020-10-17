load("@rules_cc//cc:defs.bzl", "cc_binary")

package(default_visibility = ["//visibility:public"])

cc_binary(
    name = "solver",
    srcs = ["main.cpp"],
    deps = [
        "@eigen//:eigen3",
        "@com_google_logging//:glog",
        "@com_google_absl//absl/strings"
    ],
)