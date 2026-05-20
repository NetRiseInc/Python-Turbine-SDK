SDK_TYPE := poetry
MAKEFILE_INCLUDE_DIR ?= ../../makefiles

include $(MAKEFILE_INCLUDE_DIR)/common.mk

.PHONY: generate

generate:: install
	@poetry run ariadne-codegen
