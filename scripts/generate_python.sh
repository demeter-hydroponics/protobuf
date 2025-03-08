#!/bin/sh

# make the generated folder if it doesnt already exist
mkdir -p generated/python

protoc \
--proto_path=messages \
--python_out=generated/python \
--pyi_out=generated/python \
common.proto \
node/metrics.proto node/commands.proto \
column/pump_metrics.proto column/mixing_metrics.proto column/pump_manager_info.proto column/commands.proto column/binary_load.proto \
panel/configs.proto

