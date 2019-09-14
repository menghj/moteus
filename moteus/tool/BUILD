# -*- python -*-

# Copyright 2018-2019 Josh Pieper, jjp@pobox.com.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

package(default_visibility = ["//visibility:public"])

py_library(
    name = "calibrate_encoder",
    srcs = ["calibrate_encoder.py"],
)

py_binary(
    name = "py_moteus_tool",
    srcs = ["moteus_tool.py"],
    main = "moteus_tool.py",
    deps = [
        ":calibrate_encoder",
        "//mjlib/multiplex:py_multiplex_protocol",
        "//mjlib/multiplex:aioserial",
    ],
)

cc_library(
    name = "moteus_tool_lib",
    hdrs = ["moteus_tool.h"],
    srcs = ["moteus_tool.cc"],
    deps = [
        "//mjlib/base:inplace_function",
        "//mjlib/base:program_options_archive",
        "//mjlib/base:time_conversions",
        "//mjlib/io:async_sequence",
        "//mjlib/io:stream_copy",
        "//mjlib/io:stream_factory",
        "//mjlib/multiplex:asio_client",
        "@boost//:system",
        "@com_github_serge1_elfio//:elfio",
        "@fmt",
    ],
)

cc_binary(
    name = "moteus_tool",
    srcs = ["moteus_tool_main.cc"],
    deps = [":moteus_tool_lib"],
)