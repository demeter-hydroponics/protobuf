#!/bin/sh

# grab the latest protoc
go install google.golang.org/protobuf/cmd/protoc-gen-go@latest
export PATH="$PATH:$(go env GOPATH)/bin"

# make the generated folder if it doesnt already exist
mkdir -p generated

protoc \
--proto_path=messages \
--go_out=generated \
--go_opt=paths=source_relative \
metrics/node_stats.proto common/common.proto pump/pump_stats.proto pump/mixing_stats.proto
